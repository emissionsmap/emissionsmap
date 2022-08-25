import * as THREE from 'three';
import { OrbitControls } from 'https://unpkg.com/three@0.139.2/examples/jsm/controls/OrbitControls.js';

const myCanvas = document.querySelector('#myCanvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    50,
    myCanvas.offsetWidth / myCanvas.offsetHeight, 
    // 0.1, 1000 
  );
//   camera.position.set(1, 1, 1);
//   camera.lookAt(scene.position);

const renderer = new THREE.WebGLRenderer({ canvas: myCanvas });
renderer.setClearColor(0xffffff, 1.0);
// renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(myCanvas.offsetWidth, myCanvas.offsetHeight);
// document.body.appendChild( renderer.domElement );


const imagenmundo = document.getElementById('imagenmundo');
const texture = new THREE.TextureLoader().load(imagenmundo)


const geometry = new THREE.BoxGeometry(2,2,2,5,5,5);
const material = new THREE.MeshBasicMaterial( { map:texture } );
const cube = new THREE.Mesh( geometry, material );
scene.add(cube);
camera.position.z = 5;

const orbitControls = new OrbitControls(camera, renderer.domElement);
// orbitControls.maxPolarAngle = Math.PI * 0.5;
// orbitControls.minDistance = 0.1;
// orbitControls.maxDistance = 100;
orbitControls.autoRotate = true; 
orbitControls.autoRotateSpeed = 5; 

renderer.setAnimationLoop(() => {
  orbitControls.update();

  renderer.render(scene, camera);
});




// let camera, scene, renderer;

// 			const params = {
// 				clipIntersection: true,
// 				planeConstant: 0,
// 				showHelpers: false
// 			};

// 			const clipPlanes = [
// 				new THREE.Plane( new THREE.Vector3( 1, 0, 0 ), 0 ),
// 				new THREE.Plane( new THREE.Vector3( 0, - 1, 0 ), 0 ),
// 				new THREE.Plane( new THREE.Vector3( 0, 0, - 1 ), 0 )
// 			];

// 			init();
// 			render();

// 			function init() {

// 				renderer = new THREE.WebGLRenderer({ canvas: myCanvas });
// 				renderer.setPixelRatio( window.devicePixelRatio );
// 				renderer.setSize( window.innerWidth, window.innerHeight );
// 				renderer.localClippingEnabled = true;
// 				document.body.appendChild( renderer.domElement );

// 				scene = new THREE.Scene();

// 				camera = new THREE.PerspectiveCamera( 40, window.innerWidth / window.innerHeight, 1, 200 );

// 				camera.position.set( - 1.5, 2.5, 3.0 );

// 				const controls = new OrbitControls( camera, renderer.domElement );
// 				controls.addEventListener( 'change', render ); // use only if there is no animation loop
// 				controls.minDistance = 1;
// 				controls.maxDistance = 10;
// 				controls.enablePan = false;

// 				const light = new THREE.HemisphereLight( 0xffffff, 0x080808, 1.5 );
// 				light.position.set( - 1.25, 1, 1.25 );
// 				scene.add( light );

// 				// const helper = new THREE.CameraHelper( light.shadow.camera );
// 				// scene.add( helper );

// 				//

// 				const group = new THREE.Group();

// 				for ( let i = 1; i <= 30; i += 2 ) {

// 					const geometry = new THREE.SphereGeometry( i / 30, 48, 24 );

// 					const material = new THREE.MeshLambertMaterial( {

// 						color: new THREE.Color().setHSL( Math.random(), 0.5, 0.5 ),
// 						side: THREE.DoubleSide,
// 						clippingPlanes: clipPlanes,
// 						clipIntersection: params.clipIntersection

// 					} );

// 					group.add( new THREE.Mesh( geometry, material ) );

// 				}

// 				scene.add( group );

// 				// helpers

// 				const helpers = new THREE.Group();
// 				helpers.add( new THREE.PlaneHelper( clipPlanes[ 0 ], 2, 0xff0000 ) );
// 				helpers.add( new THREE.PlaneHelper( clipPlanes[ 1 ], 2, 0x00ff00 ) );
// 				helpers.add( new THREE.PlaneHelper( clipPlanes[ 2 ], 2, 0x0000ff ) );
// 				helpers.visible = false;
// 				scene.add( helpers );

		

// 				window.addEventListener( 'resize', onWindowResize );

// 			}

// 			function onWindowResize() {

// 				camera.aspect = window.innerWidth / window.innerHeight;
// 				camera.updateProjectionMatrix();

// 				renderer.setSize( window.innerWidth, window.innerHeight );

// 				render();

// 			}

// 			function render() {

// 				renderer.render( scene, camera );

// 			}
