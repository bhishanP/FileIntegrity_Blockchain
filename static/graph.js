const container = document.getElementById("network");

const nodes = [];
const edges = [];

blockchainData.forEach((block, index) => {

    const isTampered = (systemStatus === "TAMPERED");

    const isGenesis = block.index === 1;

    nodes.push({
        id: block.index,
        label: isGenesis ? "🌟 Genesis Block" : `Block ${block.index}`,
        shape: "box",
        color: {
            background: isGenesis
                ? "#ffd700"   // gold for genesis
                : (systemStatus === "TAMPERED" ? "#ff4d4d" : "#00c6ff"),
            border: "#ffffff"
        },
        font: { color: "#000" }
    });

    if (index > 0) {
        edges.push({
            from: blockchainData[index - 1].index,
            to: block.index,
            arrows: "to"
        });
    }
});

const data = {
    nodes: new vis.DataSet(nodes),
    edges: new vis.DataSet(edges)
};

const options = {
    layout: {
        hierarchical: {
            direction: "LR",
            sortMethod: "directed"
        }
    },
    physics: false,
    edges: {
        smooth: true
    }
};

const network = new vis.Network(container, data, options);

// CLICK → OPEN MODAL
network.on("click", function (params) {
    if (params.nodes.length > 0) {
        const nodeId = params.nodes[0];
        const block = blockchainData.find(b => b.index === nodeId);

        openModal(block.index, block.merkle_root, block.previous_hash);
    }
});