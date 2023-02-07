var OutlineShader = {

	uniforms: {
		offset: { type: 'f', value: 0.01 }
	},

	vertexShader: [

		"uniform float offset;",

		"void main() {",
		"  vec4 pos = modelViewMatrix * vec4( position + normal * offset, 1.0 );",
		"  gl_Position = projectionMatrix * pos;",
		"}"

	].join('\n'),

	fragmentShader: [

		"void main() {",
		"  gl_FragColor = vec4( 0.0, 0.0, 0.0, 1.0 );",
		"}"

	].join('\n')

};

// -----------------------------------------------------

var container = document.getElementById( 'container' );

var renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setClearColor( '#ffffff', 1 );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( 600, 500 );
container.appendChild( renderer.domElement );
renderer.domElement.style.cursor = 'pointer';

var camera = new THREE.PerspectiveCamera( 40, 600 / 500, .1, 100000 );
camera.position.set( -2.0, 2.6, 3.5 );

var controls = new THREE.OrbitControls( camera, renderer.domElement );
controls.target.y = 0.9;
controls.update();
controls.enabled = false;

var scene = new THREE.Scene();

var aLight = new THREE.AmbientLight( 0x404040 );
scene.add( aLight );

var dLight = new THREE.DirectionalLight( 0xffffff, 0.6 );
dLight.position.set( 0.1, 0.7, 1 );
scene.add( dLight );

//

var fbxLoader = new THREE.FBXLoader();

var root = 'https://cdn.jsdelivr.net/gh/davidlyons/sketches@v2/2017/08fridge/';
fbxLoader.load(root + 'model/fridge.fbx', function(fbx){

	var fridgeGroup = fbx.children[0];

	var back = fridgeGroup.getObjectByName('back');
	var topDoor = fridgeGroup.getObjectByName('topDoor');
	var bottomDoor = fridgeGroup.getObjectByName('bottomDoor');
	var topHandle = fridgeGroup.getObjectByName('topHandle');
	var bottomHandle = fridgeGroup.getObjectByName('bottomHandle');

	// materials

	var fridgeMat = new THREE.MeshToonMaterial({
		color: 0xcccccc,
		shininess: 1,
		specular: 0xcccccc
	});

	var handleMat = new THREE.MeshToonMaterial({
		color: 0x777777,
		shininess: 1
	});

	back.material = topDoor.material = bottomDoor.material = fridgeMat;
	topHandle.material = bottomHandle.material = handleMat;

	// outline

	var outlineMat = new THREE.ShaderMaterial({
		uniforms: THREE.UniformsUtils.clone( OutlineShader.uniforms ),
		vertexShader: OutlineShader.vertexShader,
		fragmentShader: OutlineShader.fragmentShader,
		side: THREE.BackSide
	});

	var children = [back, topDoor, bottomDoor, topHandle, bottomHandle];
	children.forEach(function(obj){
		var outline = new THREE.Mesh( obj.geometry, outlineMat );
		obj.add( outline );
	});

	scene.add( fridgeGroup );

	topDoor.userData.isOpen = false;
	bottomDoor.userData.isOpen = false;

	// input

	function toggleDoor( door ) {

		if ( door.userData.isOpen ) {

			var close = new TWEEN.Tween( door.rotation )
				.to( { y: 0 }, 200 )
				.easing( TWEEN.Easing.Exponential.In )
				.start();

			// impact from the slam
			var slam = new TWEEN.Tween( fridgeGroup.rotation )
				.to( { y: 0 }, 200 )
				.delay( 200 )
				.easing( TWEEN.Easing.Quintic.Out )
				.start();

		} else {

			var open = new TWEEN.Tween( door.rotation )
				.to( { y: Math.PI / 2 }, 800 )
				.easing( TWEEN.Easing.Elastic.Out )
				.start();

			// so impact doesn't have to reset
			var slide = new TWEEN.Tween( fridgeGroup.rotation )
				.to( { y: THREE.Math.degToRad(10) }, 200 )
				.delay( 150 )
				.easing( TWEEN.Easing.Cubic.Out )
				.start();
		}

		door.userData.isOpen = !door.userData.isOpen;

	}

	var which = true;
	var count = 0;

	function mousedown(e){

		TWEEN.removeAll();

		var door = which ? topDoor : bottomDoor;
		door.rotation.y = door.userData.isOpen ? Math.PI / 2 : 0;

		count++;
		if ( count % 2 ) which = !which;

		door = which ? topDoor : bottomDoor;
		toggleDoor( door );

	}

	renderer.domElement.addEventListener('mousedown', mousedown, false);

});

//

window.addEventListener( 'resize', resize, false );
function resize() {
	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();
	renderer.setSize( window.innerWidth, window.innerHeight );
}

loop();

function loop() {
	requestAnimationFrame( loop );
	TWEEN.update();
	renderer.render( scene, camera );
}