
// CSRFトークンを取得する関数
function getCsrfToken() {
    const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfTokenElement ? csrfTokenElement.value : '';
}

document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button');
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-id');
            reduceStock(productId);
        });
    });
});

// 在庫減少
function reduceStock(productId) {
    fetch(`/app_folder/products/${productId}/reduce_stock/`, {
        method: 'POST',  // POSTメソッドを使用
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),  // CSRFトークンをヘッダーに追加
        },
        body: JSON.stringify({
            product_id: productId,  // POSTリクエストボディにIDを送信
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        // 成功時在庫数更新
        if (data.success) {
            location.reload();  // ページをリロードして在庫を反映
        }
    })
    .catch(error => alert("エラーが発生しました。"));
}
