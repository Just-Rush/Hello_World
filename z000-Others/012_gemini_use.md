1. 一直遇到：Failed to login. Message: This account requires setting the GOOGLE_CLOUD_PROJECT env var.   
   环境变量的问题，后解决：因为在lilux中用的，所以在win下设置环境变量没用，要在linux下设置环境变量，临时的有`export GOOGLE_CLOUD_PROJECT="你的项目ID" ` 
   永久设置可以查看zotero（就是`vim ~/.bashrc`在这里面添加上面那个就行了，这是配置环境变量的）
2. 