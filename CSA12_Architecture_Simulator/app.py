from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pipeline")
def pipeline():
    return render_template(
        "module.html",
        module="pipeline",
        title="Pipeline Analysis",
        icon="⚙️"
    )


@app.route("/cache")
def cache():
    return render_template(
        "module.html",
        module="cache",
        title="Cache & Memory Simulator",
        icon="💾"
    )


@app.route("/virtual-memory")
def virtual_memory():
    return render_template(
        "module.html",
        module="vm",
        title="Virtual Memory & TLB",
        icon="🧠"
    )


@app.route("/io-dma")
def io_dma():
    return render_template(
        "module.html",
        module="io",
        title="I/O & DMA Simulator",
        icon="🔄"
    )


@app.route("/bus")
def bus():
    return render_template(
        "module.html",
        module="bus",
        title="System Bus Analysis",
        icon="🚌"
    )


@app.route("/performance")
def performance():
    return render_template(
        "module.html",
        module="performance",
        title="Performance Evaluation",
        icon="📊"
    )


if __name__ == "__main__":
    app.run(debug=True)