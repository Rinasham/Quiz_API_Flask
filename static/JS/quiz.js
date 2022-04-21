console.log('OK');

// questionNumArr = [0,1,2,3,4,5,6,7,8,9]

let count = 3


convertData()
.then((arr)=>{
  console.log(typeof(arr));
  return showQuiz(arr)
})

function showQuiz(arr){
  if(count === 0){
    console.log('残り０問');
  } else {
    // console.log(listData[count].question);
    console.log(arr.length);
  }
}

// const random = Math.floor(Math.random() * listData.length);