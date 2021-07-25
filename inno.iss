; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Word Guide"
#define MyAppVersion "0.1"
#define MyAppPublisher "ivansaul"
#define MyAppURL "https://github.com/ivansaul"
#define MyAppExeName "main.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{74F8CCB9-683B-40CD-9670-5FED5012C39F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputBaseFilename=WordGuide-0.1
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\saul\Documents\WordGuide\output\main\{#MyAppExeName}"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_asyncio.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_bz2.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_cffi_backend.cp38-win_amd64.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_ctypes.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_decimal.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_elementtree.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_hashlib.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_lzma.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_multiprocessing.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_overlapped.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_queue.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_socket.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_ssl.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\_win32sysloader.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\avcodec-58.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\avdevice-58.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\avfilter-7.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\avformat-58.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\avutil-56.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\base_library.zip"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\glew32.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libcrypto-1_1.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libffi-7.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libfreetype-6.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libmodplug-1.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libogg-0.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libpng16-16.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libssl-1_1.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libvorbis-0.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\libvorbisfile-3.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\main.exe.manifest"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\main.kv"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\mfc140u.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\MSVCP140.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\postproc-55.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\pyexpat.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\python38.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\pythoncom38.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\pywintypes38.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\SDL2.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\SDL2_image.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\SDL2_mixer.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\SDL2_ttf.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\select.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\swresample-3.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\swscale-5.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\unicodedata.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\VCRUNTIME140.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32api.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32file.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32gui.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32trace.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32ui.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32wnet.pyd"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\zlib1.dll"; DestDir: "{localappdata}\{#MyAppName}"; Flags: ignoreversion
Source: "C:\Users\saul\Documents\WordGuide\output\main\certifi\*"; DestDir: "{localappdata}\{#MyAppName}\certifi"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\comp\*"; DestDir: "{localappdata}\{#MyAppName}\comp"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\data\*"; DestDir: "{localappdata}\{#MyAppName}\data"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\docutils\*"; DestDir: "{localappdata}\{#MyAppName}\docutils"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\ffpyplayer\*"; DestDir: "{localappdata}\{#MyAppName}\ffpyplayer"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\fonts\*"; DestDir: "{localappdata}\{#MyAppName}\fonts"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\kivy\*"; DestDir: "{localappdata}\{#MyAppName}\kivy"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\kivy_install\*"; DestDir: "{localappdata}\{#MyAppName}\kivy_install"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\kivymd\*"; DestDir: "{localappdata}\{#MyAppName}\kivymd"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\PIL\*"; DestDir: "{localappdata}\{#MyAppName}\PIL"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\saul\Documents\WordGuide\output\main\win32com\*"; DestDir: "{localappdata}\{#MyAppName}\win32com"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{localappdata}\{#MyAppName}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{localappdata}\{#MyAppName}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{localappdata}\{#MyAppName}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
