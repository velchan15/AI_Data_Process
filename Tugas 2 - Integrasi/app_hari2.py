import joblib
import pandas as pd
import gradio as gr

MODEL_FILE = "model_churn_hari2.joblib"
model = joblib.load(MODEL_FILE)

def predict_churn(age, contract, monthly_charge, tenure_months, support_calls):
    row = pd.DataFrame([{
        "age": float(age),
        "contract": str(contract),
        "monthly_charge": float(monthly_charge),
        "tenure_months": float(tenure_months),
        "support_calls": float(support_calls),
    }])
    probability = float(model.predict_proba(row)[0, 1])
    label = "RISIKO TINGGI" if probability >= 0.50 else "RISIKO RENDAH"
    return f"{label} | peluang churn: {probability:.1%}"

demo = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Slider(18, 100, value=35, step=1, label="Umur"),
        gr.Radio(["Monthly", "Annual"], value="Monthly", label="Kontrak"),
        gr.Number(value=120000, label="Tagihan bulanan"),
        gr.Slider(1, 72, value=12, step=1, label="Lama berlangganan (bulan)"),
        gr.Slider(0, 10, value=2, step=1, label="Jumlah panggilan dukungan"),
    ],
    outputs=gr.Textbox(label="Hasil prediksi"),
    title="Demo Prediksi Churn",
    description="Data sintetis untuk latihan. Hasil bukan keputusan bisnis.",
)

if __name__ == "__main__":
    demo.launch()
