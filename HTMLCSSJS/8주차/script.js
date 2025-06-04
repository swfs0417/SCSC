//변수선언언
var addclass = document.getElementById('addclass');
var deleteclass = document.getElementById('deleteclass');
var reset = document.getElementById('reset');
var classLists = document.querySelector('.class-list');
var classItem = classLists.querySelectorAll('.class-list-item');
const classList = document.querySelectorAll('.class-list-item');
const timeSchedule = document.querySelector('.time-schedule');
const timeScheduleHeader = document.querySelector('.time-schedule-header');
const credit_sum = document.getElementById('credit-sum');
let selecteditem = [];
let selectedclass = [];
let credit = 0;
let currentitem = null;

credit_sum.innerHTML = credit;

//연도 및 학기 표시시
let date = document.getElementById('date');
let d = new Date();
let current_year = d.getFullYear();
let current_semester = d.getMonth() + 1; //1 더해야 제대로 된 월이 나옴

if(current_semester< 4){
    current_semester = '1'
}else if(current_semester< 7){
    current_semester = '여름'
}else if(current_semester< 10){
    current_semester = '2'
}else{
    current_semester = '겨울'
} 

date.innerHTML = `${current_year}년 ${current_semester}학기`

const classColorMap = {
    "0": "#CD5C5C",
    "1": "#F08080",
    "2": "#FA8072",
    "3": "#E9967A",
    "4": "#FFA07A",
    "5": "#EEC2BD",
    "6": "#FFD700"
};
var colornum = 0;

// 기존 클래스에 색상 지정
let existclasscolor = document.querySelectorAll('.class-list-item-name');
for (let i = 0; i < existclasscolor.length; i++) {
    existclasscolor[i].style.backgroundColor = classColorMap[i % 7];
}

addclass.addEventListener('click', () => {
		//요소 생성하기
    let newclassitem = document.createElement('div');
    let newclassitemName = document.createElement('div');
    let newclassitemDetail = document.createElement('div');
    
    //생성된 요소에 class추가하기
    newclassitem.setAttribute('class', 'class-list-item');
    newclassitemName.setAttribute('class', 'class-list-item-name');
    newclassitemDetail.setAttribute('class', 'class-list-item-detail');
    
    newclassitemName.innerHTML = prompt('수업 이름을 입력하세요');
    newclassitem.dataset.name = newclassitemName.innerHTML;

    var day = prompt('수업 요일을 입력하세요');
    switch (day) {
        case '월': newclassitem.dataset.day = 1; break;
        case '화': newclassitem.dataset.day = 2; break;
        case '수': newclassitem.dataset.day = 3; break;
        case '목': newclassitem.dataset.day = 4; break;
        case '금': newclassitem.dataset.day = 5; break;
        case '토': newclassitem.dataset.day = 6; break;
        case '일': newclassitem.dataset.day = 7; break;
    }

    newclassitem.dataset.starttime = prompt('수업 시작 교시를 입력하세요 (숫자)');
    if (isNaN(newclassitem.dataset.starttime)) {
        alert('숫자를 입력해주세요');
        return;
    }

    newclassitem.dataset.endtime = prompt('수업 종료 교시를 입력하세요 (숫자)');
    if (isNaN(newclassitem.dataset.endtime) || newclassitem.dataset.starttime >= newclassitem.dataset.endtime) {
        alert('올바른 값을 입력해주세요');
        return;
    }

    newclassitem.dataset.credit = newclassitem.dataset.endtime - newclassitem.dataset.starttime + 1;
    newclassitemName.style.backgroundColor = classColorMap[colornum % 7];
    newclassitem.dataset.color = classColorMap[colornum % 7];
    colornum++;

    newclassitemDetail.innerHTML = `${day}요일 ${newclassitem.dataset.starttime}-${newclassitem.dataset.endtime}교시`;
    newclassitem.appendChild(newclassitemName);
    newclassitem.appendChild(newclassitemDetail);
    classLists.appendChild(newclassitem);
});

classLists.addEventListener('click', (e) => {
    if (classItem) {
        // 기존 하이라이트 제거
        for (let i = 0; i < e.currentTarget.children.length; i++) {
            e.currentTarget.children[i].classList.remove('active');
        }
        // 시간표 미리보기 초기화
        for (var i = 1; i < timeSchedule.rows.length; i++) {
            for (var j = 0; j < timeSchedule.rows[i].cells.length; j++) {
                timeSchedule.rows[i].cells[j].classList.remove('noneaddclass');
                if (!selecteditem.includes(timeSchedule.rows[i].cells[j]) && !timeSchedule.rows[i].cells[j].classList.contains('time')) {
                    timeSchedule.rows[i].cells[j].innerHTML = '';
                }
            }
        }
        // 수업 하이라이트
        var classone = e.target.closest('.class-list-item');
        classone.classList.add('active');
        currentitem = classone;
    }
        // 수업 미리보기 표시
    for (let i = currentitem.dataset.starttime; i <= currentitem.dataset.endtime; i++){
        timeSchedule.rows[i].cells[currentitem.dataset.day].classList.add('noneaddclass');
        timeSchedule.rows[i].cells[currentitem.dataset.day].innerHTML = currentitem.dataset.name;
    }
});

classLists.addEventListener('dblclick', (e) => {
    for (var i = currentitem.dataset.starttime; i <= currentitem.dataset.endtime; i++) {
        const cell = timeSchedule.rows[i].cells[currentitem.dataset.day];
        if (!cell.classList.contains('addclass')) {
            cell.innerHTML = currentitem.dataset.name;
            cell.classList.remove('noneaddclass');
            cell.classList.add('addclass');
            cell.style.backgroundColor = currentitem.dataset.color;
            selecteditem.push(cell);
        } else if (confirm('이미 수업이 있습니다. 수업을 추가하시겠습니까?')) {
            cell.innerHTML = currentitem.dataset.name;
            cell.classList.remove('noneaddclass');
            cell.classList.add('addclass');
            cell.style.backgroundColor = currentitem.dataset.color;
            selecteditem.push(cell);
        } else {
            return;
        }
    }
    selectedclass.push(currentitem);
    credit_sum_calculate();
});

deleteclass.addEventListener('dblclick', () => {
    if (currentitem) {
        currentitem.remove();
    }
});

timeSchedule.addEventListener('dblclick', (e) =>{
    if (e.target.classList.contains('addclass') && confirm('수업을 삭제하시겠습니까?')){
        const className = e.target.innerHTML;
        for (let i = 0; i < timeSchedule.rows.length; i++) {
            for(let j = 0; j < timeSchedule.rows[i].cells.length; j++) {
                const cell = timeSchedule.rows[i].cells[j];
                if (cell.innerHTML === className) {
                    cell.innerHTML = '';
                    cell.classList.remove('addclass');
                    cell.classList.remove('noneaddclass');
                    cell.style.backgroundColor = '';
                    selecteditem.splice(selecteditem.indexOf(cell), 1);
                }
            }
        }
        selectedclass = selectedclass.filter(item => item.dataset.name !== className);
        credit_sum_calculate();
    }
});

function credit_sum_calculate(){
    credit = 0;
    for (let i = 0; i < selectedclass.length; i++) {
        credit += parseInt(selectedclass[i].dataset.credit);
    }
    credit_sum.innerHTML = credit;
    if (credit > 20) {
        alert('학점이 20을 초과했습니다.');
    }
}

reset.addEventListener('click', () => {
    if( confirm('시간표를 초기화하시겠습니까?')) {
        // 시간표 초기화
        for (var i = 1; i < timeSchedule.rows.length; i++) {
            for (var j = 0; j < timeSchedule.rows[i].cells.length; j++) {
                timeSchedule.rows[i].cells[j].innerHTML = '';
                timeSchedule.rows[i].cells[j].classList.remove('addclass');
                timeSchedule.rows[i].cells[j].classList.remove('noneaddclass');
                timeSchedule.rows[i].cells[j].style.backgroundColor = '';
            }
        }
        selectedclass = [];
        selecteditem = [];
        credit_sum_calculate();
    }
});

const element = document.querySelector("#capture");
const options = {
    backgroundColor: '#ffffff',
    scale: 2
};

let capturebutton = document.querySelector('#capture-button');
capturebutton.addEventListener('click', () => {
    for (var i = 1; i < timeSchedule.rows.length; i++) {
        for (var j = 0; j < timeSchedule.rows[i].cells.length; j++) {
            timeSchedule.rows[i].cells[j].classList.remove('noneaddclass');
            if (!selecteditem.includes(timeSchedule.rows[i].cells[j])) {
                timeSchedule.rows[i].cells[j].innerHTML = ''
            }
        }
    }
    html2canvas(element, options).then(canvas => {
        console.log('찰칵');
        const imageURL = canvas.toDataURL("image/png");

        const link = document.createElement("a");
        link.href = imageURL;
        link.download = "시간표.png";
        link.click();
    });
    alert('캡쳐 완료');
});
