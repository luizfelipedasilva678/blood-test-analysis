from flask_wtf import FlaskForm
from wtforms import StringField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AnalysisForm(FlaskForm):
    title = StringField(
        "Título",
        [
            validators.DataRequired("O campo título é obrigatório"),
            validators.Length(
                min=4,
                max=25,
                message="O campo título deve ter entre 4 e 25 caracteres",
            ),
        ],
        render_kw={"placeholder": "título"},
    )
    image = FileField(
        "Exame",
        [
            FileRequired("O campo exame é obrigatório"),
            FileAllowed(
                ["jpg", "png", "jpeg", "webp"],
                "Apenas imagens (.jpg, .png, .webp, .jpeg)",
            ),
        ],
        render_kw={"placeholder": "exame"},
    )
