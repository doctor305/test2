from github3 import login  
  
gh = login('username', password='<password>')  
userinfo = gh.user()  
 
print userinfo.login  
 
print userinfo.followers  

  
  
repo=gh.repository("username","RepositoryName")  
branch=repo.branch("master")  
  
branch.links  
#它会返回：  
{u'self': u'https://api.github.com/repos/HejunweiCoder/ControlCenter/branches/master',  
u'html': u'https://github.com/HejunweiCoder/ControlCenter/tree/master'}  
  
 
def connect_to_github():  
    gh=login(username="<username>",password="<password>")  
    repo=gh.repository("<username>","<repository>")  
    branch=repo.branch("master")  
    return gh,repo,branch  
  
 def get_file_contents(filepath):  
    gh,repo,branch=connect_to_github()  
    tree=branch.commit.commit.tree.recurse()  
  
    for filename in tree.tree:  
        if filepath in filename.path:  
            print "[*] Found file %s "% filepath  
            blob=repo.blob(filename._json_data["sha"])  
            return blob.content  
  
  def store_data(data):  
    gh,repo,branch=connect_to_github()  
    remote_path = "data/test.data"  
    repo.create_file(remote_path,"Commite message",base64.b64encode(data))  
    print "upload success"  
    return
