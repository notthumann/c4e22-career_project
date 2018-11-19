from flask import Flask,render_template, request, redirect, url_for
import mlab
app = Flask(__name__)
mlab.connect()


persontype1 = {
  "name" = "The Mediator";
  "des" = "You are a sensitive idealist motivated by your deeper personal values. You see the potential of a better future, and pursue truth and meaning with your own particular flair. You love motivating others to becom better.";
  "suited" = "Graphics Designer, Psychologist, Writer, Artist, Editor, Therapist, HR development manager, Councillor";
  "point" = 10;
}

if __name__ == '__main__':
  app.run(debug=True)