


const width = document.getElementById('container').scrollWidth;
const height = document.getElementById('container').scrollHeight || 500;


// Graph实例初始化

const graph = new G6.Graph({
    container: 'container',
    width: 1000,
    height: 800,
    defaultNode: {
        type: 'circle', // 节点类型
        // ... 其他配置
      },
    layout: {
        type: 'fruchterman',
        center: [ 200, 200 ],     // 可选，默认为图的中心
        gravity: 20,              // 可选
        speed: 2,                 // 可选
        clustering: true,         // 可选
        clusterGravity: 30,       // 可选
        maxIteration: 2000,       // 可选，迭代次数
        workerEnabled: true       // 可选，开启 web-worker  
    }
    
  });

fetch('2020-02-02.json')
  .then(res => res.json())
  .then(data => {
    graph.data({
      nodes: data.nodes,
      edges: data.edges,
    });
    graph.render();

  });

