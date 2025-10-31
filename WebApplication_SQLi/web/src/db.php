<?php 
//web/src/db.php - pg_connect helper 
function make_connection($database_name = null){
    $host = getenv('DB_HOST') ?: 'db';
    $port = getenv('DB_PORT') ?: '5432';
    $user = getenv('DB_USER') ?: 'helios';
    $pass = getenv('DB_PASS') ?: 'helios123';
    $db = $database_name ?: (getenv('DB_NAME') ?: 'labdb');

    $conn_str = "host={$host} port={$port} dbname={$db} user={$user} password={$pass}";
    $conn = @pg_connect($conn_str);
    if(!$conn){
        // SỬA: Dùng biến lỗi cục bộ
        $error = error_get_last();
        error_log("PG connect failed: " . ($error['message'] ?? 'Unknown error'));
        return false;
    }
    return $conn;
}
?>