// يمكن إضافة بعض وظائف JavaScript هنا مثل التحقق من صحة النموذج أو الرسائل التفاعلية
document.querySelector("form").addEventListener("submit", function(e) {
    e.preventDefault();
    alert("تم إرسال رسالتك بنجاح!");
});
function toggleSize(section) {
    var sidebar = document.getElementById('sidebar');
    var contact = document.getElementById('contact');

    // إزالة الفئة 'active' من جميع العناصر
    sidebar.classList.remove('active');
    contact.classList.remove('active');

    // إضافة الفئة 'active' إلى العنصر الذي تم النقر عليه
    if (section === 'sidebar') {
        sidebar.classList.add('active');
    } else if (section === 'contact') {
        contact.classList.add('active');
    }
}
function toggleMenu() {
    const menu = document.getElementById("contacts-menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function addEmployee() {
    const name = prompt("أدخل اسم الموظف الجديد:");
    if (name) {
        const formData = new FormData();
        formData.append("name", name);
        fetch('/add_employee', { method: 'POST', body: formData })
            .then(res => res.text())
            .then(() => location.reload());
    }
    toggleMenu();
}

function removeEmployee() {
    alert("لم يتم تفعيل الحذف بعد.");
    toggleMenu();
}

function updateEmployee() {
    alert("لم يتم تفعيل التحديث بعد.");
    toggleMenu();
}

window.onload = function () {
    fetch('/contacts')
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById("contacts-list");
            data.forEach(emp => {
                let li = document.createElement("li");
                li.textContent = emp[1];
                li.style.padding = "10px";
                li.style.cursor = "pointer";
                li.onclick = () => {
                    displayMessage(`تم اختيار الموظف: ${emp[1]}`, 'manager');
                    scrollToBottom();
                };
                list.appendChild(li);
            });
        });
};

function sendMessage() {
    let messageInput = document.getElementById("message-input");
    let messageText = messageInput.value.trim();
    if (messageText !== "") {
        displayMessage(messageText, 'manager');
        messageInput.value = "";
        scrollToBottom();
    }
}

function sendFile(event) {
    let file = event.target.files[0];
    if (file) {
        let fileMessage = `تم إرسال ملف: ${file.name}`;
        displayMessage(fileMessage, 'manager');
        scrollToBottom();
    }
}

function displayMessage(message, sender) {
    let chatBody = document.getElementById("chat-body");
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message");
    messageDiv.classList.add(sender);
    messageDiv.innerText = message;
    chatBody.appendChild(messageDiv);
}

function scrollToBottom() {
    let chatBody = document.getElementById("chat-body");
    chatBody.scrollTop = chatBody.scrollHeight;
}
