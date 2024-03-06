
var q = 0

document.addEventListener('DOMContentLoaded', async () => {
    setInterval(checkFileOnServer, 5000);
    removeClickEventHandlers();
    checkFileOnServer()
})

async function checkFileOnServer() {
    const response = await fetch(`http://127.0.0.1:8000/images?q=${q}`,{
        method:'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    if (response.ok){
        const blob = await response.blob();
        // 이미지가 아니면 크기가 작음
        if (blob.size < 10) {
            console.log('no image response')
        }
        else {
            handleResponse(blob, q);
            q += 1
        }

    } else {
        console.error('response error');
    }
}

function handleResponse(data, q) {
    makeImgTag(q)
    const imageUrl = URL.createObjectURL(data);
    document.getElementById(`img${q}`).src = imageUrl;

    console.log('받은 응답:', data); 
}

function makeImgTag(q) {
    const listBox = document.getElementById('list-box')
    const liTag = document.createElement('li')
    const imgTag = document.createElement('img')

    liTag.classList.add('img-mini-box')
    imgTag.id = `img${q}`
    imgTag.src = ""
    imgTag.alt = "" 

    liTag.appendChild(imgTag)
    listBox.appendChild(liTag)
    addClickEventHandlers();
}


// 이전에 등록된 클릭 이벤트 핸들러 삭제하는 함수
function removeClickEventHandlers() {
    const iTags = document.querySelectorAll('ul#list-box img');
    iTags.forEach(item => {
        item.removeEventListener('click', handleImageClick);
    });
}

// 새로운 이미지에 대한 클릭 이벤트 핸들러 등록하는 함수
function addClickEventHandlers() {
    const iTags = document.querySelectorAll('ul#list-box img');
    iTags.forEach(item => {
        item.addEventListener('click', handleImageClick);
    });
}

// 이미지 클릭 이벤트 핸들러
function handleImageClick(e) {
    getImgDetail(e.target.id[-1])
    console.log('클릭된 이미지의 id:', e.target.id);
}

async function getImgDetail(imgNo) {
    const response = await fetch(`http://127.0.0.1:8000/images/detail?q=${imgNo}`,{
        method:'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    if (response.ok){
        // car img는 src긁어오기
        const plate = await response.blob();
        const detail = await response.json();
        // 이미지가 아니면 크기가 작음
        if (blob.size < 10) {
            console.log('no image response')
        }
        else {
            handleResponse(blob, detail, imgNo);
        }

    } else {
        console.error('response error');
    }
}

function handleDetailResponse(img, detail, imgNo) {
    const subImg = document.querySelector('#sub-img')
    const plate = document.querySelector('#plate')
    const logBox = document.querySelector('.log-box')
    const imageUrl = URL.createObjectURL(img);

    subImg.src = getImgSrc(imgNo)

    plate.src = imageUrl
    
    date = detail
    time = detail


    logBox.innerHTML = `
    <ul>
        <li>
            날짜
        </li>
        <li>
            ${data}
        </li>
    </ul>
    <ul>
        <li>
            시간
        </li>
        <li>
            ${time}
        </li>
    </ul>   
`
}


function getImgSrc(no) {
    return document.getElementById(`img${no}`).src

}
