<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $temp_file = $_FILES["excelFile"]["tmp_name"];

    if (file_exists($temp_file)) {
        $email = $_POST['senderEmail'];
        $sender_password = $_POST["password"];
        $message = $_POST["message"];
        $pythonScript = "emai_sending.py";
        $escaped_temp_file = escapeshellarg($temp_file);
        $escaped_email = escapeshellarg($email);
        $escaped_sender_password = escapeshellarg($sender_password);
        $escaped_message = escapeshellarg($message);

        $command = "python $pythonScript $escaped_temp_file $escaped_email $escaped_sender_password $escaped_message 2>&1";
        exec($command, $output, $return_code);

        if ($return_code === 0) {
            echo '<script>alert("Your emails were sent successfully!");</script>';
        } else {
            echo '<script>alert("Error: Something went wrong! ' . implode('\n', $output) . '");</script>';
        }
    } else {
        echo '<script>alert("Sorry, there was an error accessing the uploaded file.");</script>';
    }
} else {
    echo '<script>alert("Sorry, your file was not uploaded.");</script>';
}

echo '<script>window.location.href = "index.html"</script>';
?>
