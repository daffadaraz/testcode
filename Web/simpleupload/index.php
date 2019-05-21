<!DOCTYPE html>
<html>
    <title>Request Data</title>
    <body>
            <h2>Upload File</h2>
            <img src="https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fphotos%2Fimages%2Ffacebook%2F001%2F275%2F715%2F010.png&f=1"
            width="200" height="201">
            <form action="upload.php" method="POST" enctype="multipart/form-data"> 
                <input type="file" name="file" value="file" id="file" accept=".doc,.docx,.pdf,image/*"> 
                <br>
                <br>    
                <input type="submit" value="UPLOAD" name="submit"> 
        </form>
    <h2>List File</h2>
    </body>
</html>

<?php
$dir="Uploads"; // Directory where files are stored

if ($dir_list = opendir($dir))
{
    while(($filename = readdir($dir_list)) != false)
    {
        if($filename != '.' && $filename != '..'){
            ?>
                <p>
                    <a href="<?php echo 'uploads/'.$filename; ?>">
                    <?php echo $filename; ?>
                    </a>
                </p>
            <?php
        }
    }
    closedir($dir_list);
}
?>

<html>
    <body>
        <tfoot>
            <br><br><br><br><br>
            <p>by dapa</p>
            <p>2019</p>
        </tfoot>
    </body>
</html>