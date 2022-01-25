function calcBMI() {
  var weight = document.bmiform.pounds.value,
    height = document.bmiform.inches.value;
  document.bmiform.bmi.value = parseInt((weight * 703) / (height * height));
  if (document.bmiform.bmi.value <=18.5){
    windows.alert("Underweight");
   }
}







