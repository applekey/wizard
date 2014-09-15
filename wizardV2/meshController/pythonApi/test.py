import mmapi
from mmRemote import *;

# initialize connection
remote = mmRemote();
remote.connect();

# construct commands to run
cmd = mmapi.StoredCommands()
#cmd.AppendBeginToolCommand("planecutSO")
#cmd.AppendCompleteToolCommand("accept")
cmd.AppendSceneCommand_OpenMixFlie("c:\\scratch\\test1.mix");

# execute  commands
remote.runCommand(cmd);

#done!
remote.shutdown();

