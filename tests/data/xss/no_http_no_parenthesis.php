<html>
<body>
Hello <?php
$name = isset($_GET["name"]) ? $_GET["name"] : "anonymous coward";
if (stristr($name, "http") || stristr($name, "(")) {
    // Look mah, uber-31337 xss filtering
    $name = "anonymous hacker";
}
echo $name;
?>
</body>
</html>