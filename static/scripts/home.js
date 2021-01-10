driverBtn = document.getElementById("driver-btn")
userBtn = document.getElementById("list-btn")

userType = null

driverBtn.addEventListener("click", function() {
    userType = "driver";
});

userBtn.addEventListener("click", function() {
    userType="list";
});