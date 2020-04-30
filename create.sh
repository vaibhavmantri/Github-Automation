function github(){
    cd
    python create.py $1
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/vaibhavmantri1/$1.git
    git push -u origin master 
}                