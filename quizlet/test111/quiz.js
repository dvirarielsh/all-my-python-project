class List {
    englishlist = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj", "kkk","lll","mmm","nnn"];
    hebrewlist = ["111", "222", "333", "444", "555", "666", "777", "888", "999","100","110","120","130","140"];
    getEnglish() {
        return this.englishlist;
    }
    getHebrew() {
        return this.hebrewlist;
    }
}
let userinput = "!";
let score = document.getElementById("score")
let intscore = 0
let maxscore = 0
let question = document.getElementById("question")
let questionlist = [""]
let answerlist= [""]
let mylist = null
let englishlist = []
let hebrewlist = []
let indexofcorectans= 0
document.getElementById("submit").onclick = onEnterPress;
document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        onEnterPress();
    }
});
document.getElementById("restart").onclick = restart; 
function onEnterPress() {
    userinput = document.getElementById("getword");
    if (userinput.value==answerlist[indexofcorectans]){
        if (answerlist.length!==0){
            answerlist.splice(indexofcorectans,1)
            questionlist.splice(indexofcorectans,1)
            changescore(intscore+=1)
            addwordtothelist()
        }
        else{ 
            end()
        }
    }
    else{
        console.log(answerlist[indexofcorectans])
    }
    userinput.value = ""
    changequestion()
}
function start(){
    getthelistworldfromthejason()
    startthequeslists()
    changequestion()
    changescore(0)
}
//יסודר בהמשך החלק של הג'יסון
function getthelistworldfromthejason(){
    mylist = new List();
    englishlist = mylist.getEnglish();
    hebrewlist = mylist.getHebrew();
    maxscore = englishlist.length
}
function startthequeslists(){
    questionlist = []
    answerlist = []
    for (let i = 0; i < 10; i++) {
        addwordtothelist()
    }
}
function addwordtothelist(){
    if(englishlist.length!==0 ){
        let random = Math.floor(Math.random() * englishlist.length);
        questionlist.push(englishlist[random]);
        answerlist.push(hebrewlist[random]);
        hebrewlist.splice(random, 1);
        englishlist.splice(random, 1);
    }
}
function changequestion(){
    let random = Math.floor(Math.random() * questionlist.length);
    question.innerHTML = questionlist[random];
    indexofcorectans = random
}
function end(){
    //להוסיף פונקציה שתסיים את המשחק ותציג תוצאה אני יוסיך אחר כך
}
function changescore(intscore){
    score.innerHTML = intscore + "/" + maxscore
}
function restart(){
    intscore = 0
    start()
}
start()