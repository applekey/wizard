#ifndef _MM_STORED_COMMANDS_H__
#define _MM_STORED_COMMANDS_H__


// [RMS] #define USING_MM_COMMAND_API to use this outside of meshmixer-desktop


#include <BinarySerializer.h>

namespace mm {

class MainWindow;


struct vec3f {
	float x,y,z;
};
struct mat3f {
	float data[9];
};
struct frame3f {
	float origin_x, origin_y, origin_z;
	float normal_x, normal_y, normal_z;
	float tan1_x, tan1_y, tan1_z;
	float tan2_x, tan2_y, tan2_z;
};
struct fstring {
	unsigned int nSize;
	char data[4096];
};
struct brush_stamp {
	float x,y,z;
	float fPressure;
};


// [RMS] these are just return-type structs. we always want to use structs instead of pointers/references
//   to POD types, because SWIG will convert those pointers to arrays, and this is a mess
struct camera_info {
	float horzFOVDegrees;
	int width;
	int height;
};



class StoredCommands
{
public:
	typedef unsigned int Key;		// record-identifier returned by AppendCommand / used for GetResult



public:



	enum CommandType {
		MouseEventCommand,
		CameraControlCommand,

		ToolParameterChangeCommand,
		BeginToolCommand,
		CompleteToolCommand,
		ToolParameterCommand,

		SceneCommand,
		SelectCommand,

		BrushCommand,
		PartCommand,
		StampCommand,

		SpatialQueryCommand
	};


	/*
	 * mouse events
	 */
	void AppendMouseDownEvent( bool bLeftDown, bool bMiddleDown, bool bRightDown, float x, float y, bool bAbsolute = true );
	void AppendMouseMoveEvent( float x, float y, bool bAbsolute );
	void AppendMouseUpEvent( bool bLeftUp, bool bMiddleUp, bool bRightUp, float x, float y, bool bAbsolute );


	/*
	 * Camera manipulation
	 */
	void CameraControl_Begin();
	void CameraControl_End();
	void CameraControl_EnableOrbitSnap();
	void CameraControl_DisableOrbitSnap();
	void CameraControl_FreeOrbit(float fAngleDegreesX, float fAngleDegreesY);
	void CameraControl_TurntableOrbit(float fAngleDegreesX, float fAngleDegreesY);
	void CameraControl_Pan(float fDistanceX, float fDistanceY);
	void CameraControl_DollyZoom(float fDistanceZ);
	void CameraControl_RecenterView();
	void CameraControl_RecenterViewAtCursor();
	void CameraControl_SetSpecificView(const vec3f & eye, const vec3f & target, const vec3f & up);

	//! returned frame is eye=origin, direction=z, left=tan1, up=tan2
	Key CameraControl_QueryCamera();
	bool CameraControl_QueryCameraResult(Key k, frame3f & f, vec3f & target, camera_info & cam_info );

	Key CameraControl_QueryEyeRayAtPixel(int x, int y);
	bool CameraControl_QueryEyeRayAtPixelResult(Key k, vec3f & ray_origin, vec3f & ray_direction);

	/*
	 * INTERNAL MM TOOL API
	 */

	/*
	 * [RMS] These commands just result in calls into Qt signal handlers, IE each of these basically
	 *   mimics a GUI button-click. They may not make sense to do remotely...
	 */

	/*
	 * BeginTool command for initializing a tool. Valid tool names are:
	 *   "extrude" -			extrude selected faces
	 *   "replace" -			replace selected faces  (including fill holes)
	 *   "discard" -			discard selected faces
	 *   "createfacegroup" -	create face group
	 *   "clearfacegroup" -		clear face group
	 *   "smooth" -				smooth selected faces
	 *   "smoothboundary" -		smooth boundary loops of current selection
	 *   "deform" -				deform
	 *   "facetransform" -		transform selected faces
	 *   "faceplanecut" -		apply planar cut to selected faces
	 *   "reduce" -				reduce
	 *   "remesh" -				remesh
	 *   "extract" -			extract
	 *	 "joinboundary" -		join boundary
	 *   "stitchboundary" -		stitch boundary 
	 *   "seperate" -			seperate
	 *   "makepart" -			make part
	 *   "makepolygon" -		make polygon
	 *   "measuring" -			measuring
	 *   "inspector" -			inspector
	 *   "stability" -			stablity analysis
	 *   "overhang" -			overhang analysis
	 *   "generatefacegroup" -	generate face group
	 *   "weldcracks" -			weld cracks
	 *   "mirrorSO" -			SO mirror
	 *   "combineSO" -			combine
	 *   "duplicateSO" -		duplicate	 
	 *   "transformSO" -		SO transform
	 *   "planecutSO" -			SO plane cut
	 *   "alignSO" -			align SO
	 *   "union" -				boolean union
	 *   "difference" -			boolean difference
	 *   "intersection" -		boolean intersection
	 *   "smoothbrush" -		smooth brush
	 *   "brush" -				brush
	 *   "volbrush" -			vol brush
	 *   "stamp" -				stamp
	 *   "transform" -			transform
	 *   "setuv" -				set UV
	 *   "unifpatch" -			unify patches
	 */
	void AppendBeginToolCommand( std::string toolName );

	/*
	 * CompleteToolCommand for finishing a tool. Valid strings are:
	 *   "cancel"
	 *   "accept"
	 */
	void AppendCompleteToolCommand( std::string command );

	/*
	 * ToolParameterCommand for modifying a tool parameter. Valid parameters:
	 *   [extrude]
	        "offset" : float range [-inf, inf]
	        "harden" : float range [0,1]
	        "density" : float range [0,1]
	        "endType" values: 		Offset = 0,	Flat = 1
	        "directionType" values:	Normal = 0, Constant = 1, XAxis = 2, YAxis = 3,	ZAxis = 4
	 *   [replace]
	 		 "replaceType" values:  MinimalFill = 0, FlatRefinedMesh = 1, MVCPlanarDeformation = 2
	 		 "density" : float
	 		 "smooth" : float
	 		 "scale" : float
	 		 "boundaryRotate" : float
	 *   [discard]
	 *   [createfacegroup]
	 *   [clearfacegroup]
	 *   [smooth]
	 		 "smooth" : float
	 		 "scale" : float
	 		 "reduceType" : int
	 *   [smoothboundary]
	 		 "smoothness" : float
	 		 "preserveShape" : float
	 		 "iterations" : unsigned int
	 		 "expandLoops" : unsigned int
	 *   [deform]
	 *   [facetransform]
			"origin" :		3-float point
			"translation" :	3-float vector
			"scale" :		3-float vector
			"rotation" :	9-float 3x3 row-major matrix
	 *   [faceplanecut]
			"cutType" values: 	PreciseGeometricCut = 0, PreciseGeometricSlice = 1,	NearestPointAttach = 2,	RefinedICPAttach = 3   (default=0)
			"fillType" values: 	NoFill = 0,	CentroidRefinedFill = 1, DelaunayFill = 2,	DelaunayRefinedFill = 3  (default=3)
			"hardEdge" : boolean
			"origin" : 3-float point
			"normal" : 3-float vector
			"rotation" : 9-float 3x3 row-major matrix
	 *   [reduce]
	 		 "density" : float
	 		 "smooth" : float
	 		 "normalThreshold" : float
	 		 "reduceType" values: Uniform = 0,	 Adaptive_Normal = 1
	 *   [remesh]
	 		 "density" : float
	 		 "smooth" : float
	 		 "normalThreshold" : float
	 		 "remeshType" values: Uniform = 0,	 Adaptive_Normal = 1
	 *   [extract]
	 		 "offset" : float
	 		 "endType" values: OffsetDistance = 0,	 PlanarFlat = 1
	 		 "directionType" values: NormalDirection = 0,	 ConstantDirection = 1,	 UnitXDirection = 2,	 UnitYDirection = 3,	 UnitZDirection = 4
	 *	 [joinboundary]
	 *   [stitchboundary]
	 		 "tolerance" in float
	 *   [seperate]
	 *   [makepart]
	 *   [makepolygon]
	 *   [measuring]
	 *   [inspector]
	 *   [stability]
	 		 "contactTolerance"	: float
	 *   [overhang]
	 		 "overhangAngleTolerance" : float
	 		 "contactTolerance": float
	 *   [generatefacegroup]
	 		 "angleThreshold" : float
	 *   [weldcracks]
	 *   [mirrorSO] 
	 *   [combineSO]
	 *   [duplicateSO]
	 *   [transformSO]
	 *   [planecutSO]
			"cutType" values: 	PreciseGeometricCut = 0, PreciseGeometricSlice = 1,	NearestPointAttach = 2,	RefinedICPAttach = 3   (default=0)
			"fillType" values: 	NoFill = 0,	CentroidRefinedFill = 1, DelaunayFill = 2,	DelaunayRefinedFill = 3  (default=3)
			"hardEdge" : boolean
			"origin" : 3-float point
			"normal" : 3-float vector
			"rotation" : 9-float 3x3 row-major matrix
	 *   [alignSO]
	 *   [boolean]
	 *   [smoothbrush]
	 *   [brush]
	 *   [volumebrush]
	 		"strength" : float range [0,1]
	 		"size" : float range [ModelSize*0.00001f, ModelSize*0.2f]
	 		"depth" : float range [-1,1]
	 		"lazyness" : float range [0,1]
	 		"volumetric" : bool
	 		"symmetric" : bool
	 		"surfSnap" : bool
	 		"continuous" : bool
	 		"restrictToGroup" : bool
	 		"holdBoundary" : bool
	 		"enableRefinement" : bool
	 		"refine" : float range [0,1]
	 		"reduce" : float range [0,1]
	 		"refineSmooth" : float range [0,1]
	 *   [stamp]
	 		 "snapDimension" : bool
	 *   [setuv]
	 		 "mapType" values: DiscreteNaturalConformal, AsRigidAsPossible
	 		 "inputSmoothingAlpha" : float
	 *   [unifypatches]
	 */
	void AppendToolParameterCommand( std::string paramName, float fValue );
	void AppendToolParameterCommand( std::string paramName, int nValue );
	void AppendToolParameterCommand( std::string paramName, bool bValue );
	void AppendToolParameterCommand( std::string paramName, float x, float y, float z );
	void AppendToolParameterCommand( std::string paramName, float m00, float m01, float m02, float m10, float m11, float m12, float m20, float m21, float m22 );






	/*
	 * CLEAN MM API
	 * [RMS] this is essentially a procedural modeling API...
	 */


	/*
	 * SCENE COMMANDS
	 */

	void AppendSceneCommand_Clear();

	Key AppendSceneCommand_AppendMeshFile( const char * pFilename );
	bool GetSceneCommandResult_AppendMeshFile( Key k, std::vector<int> & vObjects );


	/*
	 * QUERY COMMANDS
	 */

	// get bounding box
	Key AppendQueryCommand_GetBoundingBox();
	bool GetQueryResult_GetBoundingBox( Key k, float fMin[3], float fMax[3] );

	// find nearest point on selected object
	Key AppendQueryCommand_FindRayIntersection( float ox, float oy, float oz, float dx, float dy, float dz );
	Key AppendQueryCommand_FindRayIntersection( const vec3f & o, const vec3f & d );
	bool GetQueryResult_FindRayIntersection( Key k, frame3f * pFrame );


	// find nearest point on selected object
	Key AppendQueryCommand_FindNearestPoint( float x, float y, float z );
	Key AppendQueryCommand_FindNearestPoint( const vec3f & p );
	bool GetQueryResult_FindNearestPoint( Key k, frame3f * pFrame );


	/*
	 *  SELECTION COMMANDS
	 */

	void AppendSelectCommand_All( );

	// parameter is 3D point
	Key AppendSelectCommand_NearestComponent( float cx, float cy, float cz );
	Key AppendSelectCommand_ContainingComponent( float cx, float cy, float cz );

	// parameters are ray origin & direction
	Key AppendSelectCommand_FirstComponentIntersectingRay( float ox, float oy, float oz, float dx, float dy, float dz );
	Key AppendSelectCommand_AllComponentsIntersectingRay( float ox, float oy, float oz, float dx, float dy, float dz );

	// parameter is sphere center/radius
	Key AppendSelectCommand_InsideSphere( float cx, float cy, float cz, float r );
	bool GetSelectCommandResult_InsideSphere( Key k );

	Key AppendSelectCommand_ByFaceGroups( const std::vector<int> & vGroupIDs );
	bool GetSelectCommandResult_ByFaceGroups( Key k );


	/*
	 *  ACTION COMMANDS
	 */

	Key AppendActionCommand_BrushStroke3D( const std::vector<brush_stamp> & vPoints );


	/* Part Drop. During interactive part drop you can also use AppendToolParameterCommand() with following parameters:
			"radius" : float range [0, inf]
			"angle" : float range [0, 2pi]
			"position" : 3-float point   *** must be point on surface ***

			"deformType" : values  COILS = 0, RotInvCoord = 1  (default=0)
			"optimize" : boolean
			"bend" : float range [0, inf]
			"bulge" : float range [-180,180]
			"offset" : float range [-inf, inf]
			"scale" : float range [0.0001, inf]
			"scaleFalloff" : float range [0.0001, 1]

			"smoothRadius" : float range [0, inf]
			"tweakRaduis" : float range [0.0001, inf]
	*/
	Key AppendActionCommand_DropPartAtPoint( const char * pPartPath, const frame3f & f, float fRadius, bool bInteractive = false );
	Key AppendActionCommand_UpdateDropPart( const frame3f & f, float fRadius, bool bMinimizeRotation );
	Key AppendActionCommand_AcceptDropPart( );
	// [RMS] for any of above, returns whether drop was successful or not. Only returns new GroupIDs when drop is completed
	bool GetActionCommandResult_DropPart( Key k, std::vector<int> & vNewGroups );

	Key AppendActionCommand_InsertPolygon( float x, float y, float z, float fRadius );
	bool GetActionCommandResult_InsertPolygon( Key k, int & nNewGroupID );





	/*
	 * Serialization / Execution
	 */

	void Store(rms::BinarySerializer & s);
	void Restore(rms::BinarySerializer & s);
	void Restore(unsigned char * pBytes, size_t nSize);

	void Execute(MainWindow * pMainWin);

	void Store_Results(rms::BinarySerializer & s);
	void Restore_Results(rms::BinarySerializer & s);
	void Restore_Results(unsigned char * pBytes, size_t nSize);

	void Store_Internal();
	size_t Store_GetSize();
	void Store_GetBuffer(unsigned char * pBytes, size_t nSize );


public:
	struct vector_int {
		unsigned int nElements;
		int data[4096];
		vector_int & append(int i);
	};
	struct vector_float {
		unsigned int nElements;
		float data[4096];
		vector_float & append(float f);
	};

private:

	enum MouseEventType {
		MouseDown, MouseMove, MouseUp
	};
	struct MouseEvent {
		MouseEventType eType;
		bool bLeft, bRight, bMiddle;
		float x,y;
		bool bCoordIsAbsolute;

		// cannot have constructor because we are putting this in union...
		void init() { eType = MouseMove; bLeft = bRight = bMiddle = false; x = y = 0; bCoordIsAbsolute = true; }
	};



	enum CameraCmdType {
		CamManip, CamToggleSnap, CamOrbit, CamTurntable, CamPan, CamDolly, CamRecenter, CamSet, CamQuery, CamGetRay
	};
	struct CameraCmd {
		CameraCmdType eType;
		float fVal1, fVal2;
		vec3f eye, target, up;
		bool bFlag;
		int nx, ny;
	};
	struct CameraCmdResult {
		frame3f f;
		vec3f target;
		float fov;
		int nx, ny;
	};



	struct ToolStringCmd {
		char name[32];
	};

	struct ToolParamValueCmd {
		char name[32];
		char eType;		// 0 = float, 1 = int, 2 = bool
		union {
			float f;
			int i;
			vec3f vec;
			mat3f mat3;
		} v;
	};



	enum SceneCmdType {
		ClearScene,
		AppendMeshFile
	};
	struct SceneCmd {
		SceneCmdType eType;
		fstring filename;
	};
	struct SceneCmdResult {
		int OK;
		vector_int nObjectIDs;
	};



	enum SelectCmdType {
		SelectAll,
		
		SelectNearestComponent,
		SelectContainingComponent,
		SelectFirstComponentIntersectingRay,
		SelectAllComponentsIntersectingRay,

		SelectInsideSphere,
		SelectFaceGroups
	};
	struct SelectCmd {
		SelectCmdType eType;
		vec3f p;
		vec3f d;
		float r;
		vector_int vGroups;
	};
	struct SelectCmdResult {
		int OK;
	};


	enum BrushCmdType {
		Stroke3D
	};
	struct BrushCmd {
		BrushCmdType eType;
		vector_float vStamps;
	};



	enum PartCmdType {
		DropPart, UpdatePart, AcceptPart
	};
	struct PartCmd {
		PartCmdType eType;
		fstring filename;
		frame3f f;
		float r;
		bool bFlag;
	};
	struct PartCmdResult {
		int OK;
		vector_int vNewGroups;
	};


	enum StampCmdType {
		InsertPolygonStamp
	};
	struct StampCmd {
		StampCmdType eType;
		float x,y,z;
		float r;
	};
	struct StampCmdResult {
		int OK;
		int nNewGroupID;
	};


private:
	enum SpatialQueryType {
		BoundingBoxQuery,
		NearestPointSpatialQuery,
		RayIntersectionSpatialQuery
	};
	struct SpatialQueryCmd {
		SpatialQueryType eType;
		vec3f p;
		vec3f d;
	};
	struct SpatialQueryResult {
		int OK;
		vector_float v;
	};


	struct Command {
		CommandType eType;
		union {
			MouseEvent mouse;
			CameraCmd camera;

			ToolStringCmd toolctrl;
			ToolParamValueCmd toolparam;

			SceneCmd scene;
			SelectCmd select;

			BrushCmd brush;
			PartCmd part;
			StampCmd stamp;

			SpatialQueryCmd spatial;
		} c;
		union {
			CameraCmdResult camera;

			SceneCmdResult scene;
			SelectCmdResult select;

			PartCmdResult part;
			StampCmdResult stamp;

			SpatialQueryResult spatial;
		} r;

		void init();			// clear all data files
	};
	std::vector<Command> m_vCommands;


	bool Execute_IO(MainWindow * pMainWin, unsigned int k);
	bool Execute_Scene(MainWindow * pMainWin, unsigned int k);
	bool Execute_Select(MainWindow * pMainWin, unsigned int k);
	bool Execute_Tool(MainWindow * pMainWin, unsigned int k);
	bool Execute_Query(MainWindow * pMainWin, unsigned int k);

	rms::BinarySerializer m_internalStore;
};





}   // end namespace mm

#endif // _MM_STORED_COMMANDS_H__