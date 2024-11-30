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
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        // 成功時在庫数更新
        if (data.success) {
            location.reload();
        }
    })
    .catch(error => alert("エラーが発生しました。"));
}
