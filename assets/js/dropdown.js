//Sidebar dropdown 
const buttons = document.getElementsByClassName("sidebar-dropdown-btn");

Array.from(buttons).forEach(button => {
    button.addEventListener("click", () => {
        const dropdown = button.parentElement.querySelector(".sidebar-dropdown");
        const icon = button.querySelector('i');
        let toggle = dropdown.style.height;

        icon.style.transform = `rotate(${toggle ? 0 : 180}deg)`;
        dropdown.style.height = toggle ? null : dropdown.scrollHeight + "px";
    });
});