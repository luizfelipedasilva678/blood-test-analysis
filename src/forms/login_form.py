from wtforms import StringField, PasswordField, validators
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField(
        "Usuário",
        [
            validators.DataRequired("O campo usuário é obrigatório"),
            validators.Length(
                min=4,
                max=25,
                message="O campo usuário deve ter entre 4 e 25 caracteres",
            ),
        ],
        render_kw={"placeholder": "seu usuário"},
    )
    password = PasswordField(
        "Senha",
        [
            validators.DataRequired("O campo senha é obrigatório"),
            validators.Length(
                min=8, max=25, message="O campo senha deve ter entre 8 e 25 caracteres"
            ),
        ],
        render_kw={"placeholder": "sua senha"},
    )
