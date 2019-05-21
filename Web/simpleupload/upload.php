<?php
if(isset($_POST['submit'])){
    $file = $_FILES['file'];
    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name'];
    $fileSize = $_FILES['file']['size'];
    $fileError = $_FILES['file']['error'];
    $fileType = $_FILES['file']['type'];

    $fileExt = explode('.',$fileName);
    $fileActualExt = strtolower(end($fileExt));

    $allowed = array('doc','docx','pdf','png','jpg','jpeg');

    if(in_array($fileActualExt,$allowed)){
        if($fileError === 0){
            if($fileSize < 10000000 ){
                $fileDest = 'uploads/'.$fileName;
                move_uploaded_file($fileTmpName,$fileDest);
                header("Location: success.php");
            }
            else{
                echo "File terlalu besar. (max. 10mb)";
            }
        } else{
            echo "Error saat mengupload.";
        }
    }
    else{
        echo "Hanya menerima file .doc .docx dan .pdf";
    }
}
?>