document.addEventListener("DOMContentLoaded", function () {
    const memoInput = document.getElementById("memo-input");
    const addMemoButton = document.getElementById("add-memo");
    const memoList = document.getElementById("memo-list");

    function saveMemos() {
        const memos = [];
        document.querySelectorAll("#memo-list li").forEach(memo => {
            memos.push(memo.textContent.replace("🗑️", "").trim());
        });
        localStorage.setItem("memos", JSON.stringify(memos));
    }

    function loadMemos() {
        const savedMemos = JSON.parse(localStorage.getItem("memos")) || [];
        savedMemos.forEach(memo => addMemo(memo));
    }

    function addMemo(text) {
        const li = document.createElement("li");
        li.textContent = text;
        
        const deleteButton = document.createElement("span");
        deleteButton.textContent = "🗑️";
        deleteButton.style.cursor = "pointer";
        deleteButton.onclick = function () {
            li.remove();
            saveMemos();
        };
        
        li.appendChild(deleteButton);
        memoList.appendChild(li);
        saveMemos();
    }

    addMemoButton.addEventListener("mouseover", function () {
        addMemoButton.textContent = "Click!";
    });

    addMemoButton.addEventListener("mouseout", function () {
        addMemoButton.textContent = "Memo Add!";
    });
    
    
    addMemoButton.addEventListener("click", function () {
        const text = memoInput.value.trim();
        if (text) {
            addMemo(text);
            memoInput.value = "";
        }
    });

    loadMemos();
});
