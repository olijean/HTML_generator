class HtmlPage():

    def __init__(self, title, background_image_path, file_name):
        self.title = title
        self.background_image_path = background_image_path
        self.file_name = file_name

        html_code = self.write_string_hmtl()
        self.write_html_file(self.file_name, html_code)
    
    def write_string_hmtl(self):

        meta = """<!DOCTYPE html>
                    
<html>
    <meta charset="utf-8">
    <meta name='description' content="Recettes">
    <title>Les meilleures recettes</title>


    <link href="https://fonts.googleapis.com/css?family=Lobster" rel='stylesheet' type='text/css'>\n"""

        style = """    <style>
            body{
                background-image: url('"""+self.background_image_path+"""');
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: cover;
            }

            .sidenav{
                font-size: 30px;
                background-color: beige;
                border-style: groove;
                height: 100%;
                width: 10%;
                padding: 8px 8px 8px 8px;
            }

            .text_black{
                color: black;
            }

            h1 {
                font-family: Lobster, monospace;
            }

            .container {
                position: relative;
                width: 200px;
                border-style: inset;
                border-color: beige;
            }

            .image {
                display: block;
                width: 200px;
                height: auto;
            }

            .overlay {
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                height: 100%;
                width: 100%;
                opacity: 0;
                transition: .5s ease;
                background-color: beige;
                cursor: pointer;
            }

            .container:hover .overlay {
                opacity: 1;
            }

            .text {
                color: black;
                font-size: 20px;
                position: absolute;
                top: 50%;
                left: 50%;
                -webkit-transform: translate(-50%, -50%);
                -ms-transform: translate(-50%, -50%);
                transform: translate(-50%, -50%);
                text-align: center;
            }

            .center{
                margin-left: 25%;
                margin-right: auto;
            }

    </style>\n"""

        header = """    <header>
        <center>
            <h1 style="padding-top: 2px; padding-bottom: 2px; background-color: beige; border-style: double; border-color: black; font-size: 40px;">"""+self.title+"""</h1>
        </center>

    </header>\n"""

        body = """    <body>

        <div class='container center' onclick="location.href='entree.html'">
            <img src='image/entree.jpg' alt='entree' class='image'>
            <div class='overlay'>
                <div class='text'>Entree</div>
            </div>
        </div>
        <br/>
        <div class='container center' onclick="location.href='principal.html'">
            <img src='image/repas_principal.jpg' alt='entree' class='image'>
            <div class='overlay'>
                <div class='text'>Repas principal</div>
            </div>
        </div>
        <br/>
        <div class='container center' onclick="location.href='dessert.html'">
            <img src='image/dessert.jpg' alt='entree' class='image'>
            <div class='overlay'>
                <div class='text'>Dessert</div>
            </div>
        </div>

    </body>\n"""

        close_hmtl = '</html>'

        return meta + style + header + body + close_hmtl

    def write_html_file(self, file_name, html_code):

        Html_file= open(file_name,"w")
        Html_file.write(html_code)
        Html_file.close()


if __name__ == "__main__":

    HtmlPage("RECETTE DE LA BOMBE", "image/bombe.jpg", "recette/bombe.html")

