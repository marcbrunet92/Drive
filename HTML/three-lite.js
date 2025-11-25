
export class Vector3 {
    constructor(x=0,y=0,z=0){this.x=x;this.y=y;this.z=z}
    set(x,y,z){this.x=x;this.y=y;this.z=z;return this}
}

export class BufferAttribute {
    constructor(array, itemSize){ this.array = array; this.itemSize = itemSize }
}

export class BufferGeometry {
    constructor(){ this.attributes = {}; }
    setAttribute(name, attr){ this.attributes[name]=attr }
}

export class PlaneGeometry extends BufferGeometry {
    constructor(w=1,h=1){
        super();
        const positions = new Float32Array([
            -w/2, -h/2, 0,
            w/2, -h/2, 0,
            w/2,  h/2, 0,
            -w/2,  h/2, 0
        ]);
        const uvs = new Float32Array([
            0,0, 1,0, 1,1, 0,1
        ]);
        const indices = new Uint16Array([0,1,2, 0,2,3]);
        this.setAttribute('position', new BufferAttribute(positions, 3));
        this.setAttribute('uv', new BufferAttribute(uvs, 2));
        this.index = indices;
    }
}

export class PointsGeometry extends BufferGeometry {
    constructor(positionsArray){ super(); this.setAttribute('position', new BufferAttribute(new Float32Array(positionsArray),3)) }
}

export class Material {
    constructor(){ this.transparent=false }
}

export class MeshLambertMaterial extends Material {
    constructor(params={}){ super(); this.map = params.map||null; this.transparent = !!params.transparent; this.opacity = params.opacity===undefined?1:params.opacity }
}

export class PointsMaterial extends Material {
    constructor(params={}){ super(); this.size = params.size||1; this.color = params.color||0xffffff; this.transparent = !!params.transparent }
}

export class Object3D {
    constructor(){ this.position = new Vector3(); this.rotation = new Vector3(); this.scale = new Vector3(1,1,1); this.children = []; this.matrixWorld = null; this.visible = true }
    add(c){ this.children.push(c); c.parent = this }
}

export class Mesh extends Object3D {
    constructor(geometry, material){ super(); this.geometry = geometry; this.material = material }
}

export class Points extends Object3D {
    constructor(geometry, material){ super(); this.geometry = geometry; this.material = material }
}

export class Scene extends Object3D {
    constructor(){ super(); this.fog = null }
}

export class FogExp2 { constructor(color=0x000000, density=0.002){ this.color = color; this.density = density } }

export class PerspectiveCamera {
    constructor(fov=60, aspect=1, near=0.1, far=2000){ this.fov=fov; this.aspect=aspect; this.near=near; this.far=far; this.position = new Vector3(); this.rotation = new Vector3() }
    updateProjectionMatrix(){ /* no-op for this tiny renderer */ }
}

export class AmbientLight { constructor(color=0xffffff,intensity=1){ this.color = color; this.intensity = intensity } }
export class DirectionalLight { constructor(color=0xffffff,intensity=1){ this.color=color; this.intensity=intensity; this.position=new Vector3() } }
export class PointLight { constructor(color=0xffffff,intensity=1,distance=0,decay=1){ this.color=color; this.intensity=intensity; this.position=new Vector3(); this.distance=distance; this.decay=decay } }

export class TextureLoader {
    load(url, onLoad){ const img = new Image(); img.crossOrigin = 'anonymous'; img.onload = ()=> onLoad({image: img}); img.src = url }
}

// Small WebGL helper functions
function createShader(gl, type, src){ const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); if(!gl.getShaderParameter(s, gl.COMPILE_STATUS)){ console.error(gl.getShaderInfoLog(s)); gl.deleteShader(s); return null } return s }
function createProgram(gl, vs, fs){ const vsS = createShader(gl, gl.VERTEX_SHADER, vs); const fsS = createShader(gl, gl.FRAGMENT_SHADER, fs); const prog = gl.createProgram(); gl.attachShader(prog, vsS); gl.attachShader(prog, fsS); gl.linkProgram(prog); if(!gl.getProgramParameter(prog, gl.LINK_STATUS)){ console.error(gl.getProgramInfoLog(prog)); gl.deleteProgram(prog); return null } return prog }

// Shaders: textured quad for Mesh + simple lambert using directional+ambient+point
const meshVS = `#version 100
attribute vec3 position; attribute vec2 uv; uniform mat4 modelViewMatrix; uniform mat4 projectionMatrix; varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`;
const meshFS = `#version 100
precision mediump float; varying vec2 vUv; uniform sampler2D map; uniform vec3 ambientColor; uniform float ambientIntensity; uniform vec3 dirColor; uniform float dirIntensity; uniform vec3 dirPos; uniform float opacity; void main(){ vec4 tex = texture2D(map, vUv); vec3 color = tex.rgb * (ambientColor * ambientIntensity + dirColor * dirIntensity * max(dot(normalize(dirPos), vec3(0.,0.,1.)), 0.)); gl_FragColor = vec4(color, tex.a * opacity); }`;

// Points shader
const pointsVS = `#version 100
attribute vec3 position; attribute float size; uniform mat4 modelViewMatrix; uniform mat4 projectionMatrix; void main(){ gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); gl_PointSize = size; }`;
const pointsFS = `#version 100
precision mediump float; uniform vec3 color; void main(){ float d = length(gl_PointCoord - vec2(0.5)); if(d>0.5) discard; gl_FragColor = vec4(color,1.0); }`;

export class WebGLRenderer {
    constructor(options={}){
        this.canvas = document.createElement('canvas'); this.gl = this.canvas.getContext('webgl',{alpha:true}); this.domElement = this.canvas; this._size = {w:300,h:150};
        // compile programs
        this._meshProgram = createProgram(this.gl, meshVS, meshFS);
        this._pointsProgram = createProgram(this.gl, pointsVS, pointsFS);
        this._textures = new WeakMap();
    }
    setSize(w,h){ this._size.w=w; this._size.h=h; this.canvas.width=w; this.canvas.height=h; this.gl.viewport(0,0,w,h) }
    setClearColor(color){ // color as 0xRRGGBB
        const r = ((color>>16)&255)/255, g = ((color>>8)&255)/255, b = (color&255)/255; this._clearColor=[r,g,b,1] }
    _useTexture(texObj){ if(!texObj) return null; const gl = this.gl; if(this._textures.has(texObj)) return this._textures.get(texObj); const tex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex); gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR); gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE, texObj.image); this._textures.set(texObj, tex); return tex }
    render(scene, camera){ const gl = this.gl; const cc = this._clearColor||[0,0,0,1]; gl.clearColor(cc[0],cc[1],cc[2],cc[3]); gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        // simple projection matrix
        const aspect = this._size.w / this._size.h; const fov = camera.fov * Math.PI/180; const f = 1.0/Math.tan(fov/2);
        const proj = new Float32Array([f/aspect,0,0,0, 0,f,0,0, 0,0,(camera.far+camera.near)/(camera.near-camera.far),-1, 0,0,(2*camera.far*camera.near)/(camera.near-camera.far),0]);
        // traverse scene
        const ambient = {color:[0,0,0], intensity:0}; const directional = {color:[1,1,1], intensity:0, pos:[0,0,1]}; let pointLight = null;
        for(const c of scene.children){ if(c instanceof AmbientLight){ const col=c.color; ambient.color=[((col>>16)&255)/255,((col>>8)&255)/255,(col&255)/255]; ambient.intensity = c.intensity } if(c instanceof DirectionalLight){ const col=c.color; directional.color=[((col>>16)&255)/255,((col>>8)&255)/255,(col&255)/255]; directional.intensity=c.intensity; directional.pos=[c.position.x,c.position.y,c.position.z] } if(c instanceof PointLight){ pointLight = c } }
        // draw meshes
        for(const obj of scene.children){ if(!obj.visible) continue; if(obj instanceof Mesh){ const prog = this._meshProgram; gl.useProgram(prog);
            // attributes
            const posAttr = obj.geometry.attributes.position; const uvAttr = obj.geometry.attributes.uv;
            const posLoc = gl.getAttribLocation(prog,'position'); const uvLoc = gl.getAttribLocation(prog,'uv');
            const vb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,vb); gl.bufferData(gl.ARRAY_BUFFER,posAttr.array,gl.STATIC_DRAW); gl.enableVertexAttribArray(posLoc); gl.vertexAttribPointer(posLoc, posAttr.itemSize, gl.FLOAT, false, 0,0);
            const ub = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,ub); gl.bufferData(gl.ARRAY_BUFFER,uvAttr.array,gl.STATIC_DRAW); gl.enableVertexAttribArray(uvLoc); gl.vertexAttribPointer(uvLoc, uvAttr.itemSize, gl.FLOAT, false, 0,0);
            const ib = gl.createBuffer(); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, obj.geometry.index, gl.STATIC_DRAW);
            // uniforms
            const mvLoc = gl.getUniformLocation(prog,'modelViewMatrix'); const pLoc = gl.getUniformLocation(prog,'projectionMatrix');
            const ambientColorLoc = gl.getUniformLocation(prog,'ambientColor'); const ambientIntLoc = gl.getUniformLocation(prog,'ambientIntensity');
            const dirColorLoc = gl.getUniformLocation(prog,'dirColor'); const dirIntLoc = gl.getUniformLocation(prog,'dirIntensity'); const dirPosLoc = gl.getUniformLocation(prog,'dirPos'); const opacityLoc = gl.getUniformLocation(prog,'opacity');
            // simple modelView = identity translated by position
            const tx = obj.position.x, ty=obj.position.y, tz=obj.position.z;
            const modelView = new Float32Array([1,0,0,0, 0,1,0,0, 0,0,1,0, tx,ty,tz,1]);
            gl.uniformMatrix4fv(mvLoc,false,modelView); gl.uniformMatrix4fv(pLoc,false,proj);
            gl.uniform3fv(ambientColorLoc,new Float32Array(ambient.color)); gl.uniform1f(ambientIntLoc, ambient.intensity);
            gl.uniform3fv(dirColorLoc,new Float32Array(directional.color)); gl.uniform1f(dirIntLoc, directional.intensity); gl.uniform3fv(dirPosLoc,new Float32Array(directional.pos)); gl.uniform1f(opacityLoc, obj.material.opacity===undefined?1:obj.material.opacity);
            // texture
            if(obj.material.map) {
                const tex = this._useTexture(obj.material.map);
                const mapLoc = gl.getUniformLocation(prog,'map'); gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE0, tex); gl.uniform1i(mapLoc,0);
            }
            gl.drawElements(gl.TRIANGLES, obj.geometry.index.length, gl.UNSIGNED_SHORT, 0);
        } else if(obj instanceof Points){ const prog = this._pointsProgram; gl.useProgram(prog);
            const posAttr = obj.geometry.attributes.position; const posLoc = gl.getAttribLocation(prog,'position'); const sizeLoc = gl.getAttribLocation(prog,'size');
            const vb = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER,vb); gl.bufferData(gl.ARRAY_BUFFER,posAttr.array,gl.STATIC_DRAW); gl.enableVertexAttribArray(posLoc); gl.vertexAttribPointer(posLoc, posAttr.itemSize, gl.FLOAT, false, 0,0);
            // size: use constant
            const sizeUniformLoc = gl.getUniformLocation(prog,'size'); const colorLoc = gl.getUniformLocation(prog,'color');
            gl.uniform3fv(colorLoc, new Float32Array([((obj.material.color>>16)&255)/255,((obj.material.color>>8)&255)/255,(obj.material.color&255)/255]));
            // set matrices
            const mvLoc = gl.getUniformLocation(prog,'modelViewMatrix'); const pLoc = gl.getUniformLocation(prog,'projectionMatrix');
            const modelView = new Float32Array([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]);
            gl.uniformMatrix4fv(mvLoc,false,modelView); gl.uniformMatrix4fv(pLoc,false,proj);
            gl.drawArrays(gl.POINTS, 0, posAttr.array.length/3);
        }}
    }
}

// END of three-lite.js
