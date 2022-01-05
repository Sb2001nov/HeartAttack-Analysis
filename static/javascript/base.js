var mybutton = document.getElementById("submit");

function show() {
  age = document.querySelector("#age").value;
  sex = document.querySelector("#sex").value;
  cp = document.querySelector("#cp").value;
  trtbps = document.querySelector("#trtbps").value;
  chol = document.querySelector("#chol").value;
  fbs = document.querySelector("#fbs").value;
  rest_ecg = document.querySelector("#rest_ecg").value;
  thalachh = document.querySelector("#thalach").value;
  exng = document.querySelector("#exang").value;
  oldpeak = document.querySelector("#oldpeak").value;
  slp = document.querySelector("#slp").value;
  caa = document.querySelector("#caa").value;
  thall = document.querySelector("#thall").value;

  const url = `https://hearthealthml.herokuapp.com/api/?age=${age}&sex=${sex}&cp=${cp}&trtbps=${trtbps}&chol=${chol}&fbs=${fbs}&restecg=${rest_ecg}&thalachh=${thalachh}&exng=${exng}&oldpeak=${oldpeak}&slp=${slp}&caa=${caa}&thall=${thall}`;

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      render(data["result"]);
    });
}

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  show();
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

function render(value) {
  var tag = document.createElement("p");
  if (value == 1) {
    var text = document.createTextNode(
      `there are high chances that you might have heart related diseases`
    );
  } else if (value == 0) {
    var text = document.createTextNode(
      `there are low chances that you might have heart related diseases`
    );
  } else {
    var text = document.createTextNode(value);
  }

  tag.appendChild(text);
  var element = document.getElementById("result");
  element.appendChild(tag);
}
