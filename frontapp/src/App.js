// src/App.js

import "./App.css";
import { useState } from "react";

function App() {
  const [producto, setProducto] = useState("");
  const [precio, setPrecio] = useState("");
  const [inventario, setInventario] = useState("");
  const [message, setMessage] = useState("");

  let handleSubmit = async (e) => {
    console.log('tetet')
    e.preventDefault();
    try {
      if(producto != '' & precio != '' & inventario != ''){
      let res = await fetch("http://127.0.0.1:5000/inventario/agregar", {
        method: "PUT",
        body: JSON.stringify({
          producto: producto,
          precio: precio,
          inventario: inventario,
        }),
      });
      let resJson = await res.json();
      if (res.status === 200) {
        setProducto("");
        setPrecio("");
        setInventario("");
        setMessage("Producto agregado con exito");
      } else {
        setMessage("Error!");
      }
    }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={producto}
          placeholder="Producto"
          onChange={(e) => setProducto(e.target.value)}
        />
        <input
          type="float"
          value={precio}
          placeholder="Precio"
          onChange={(e) => setPrecio(e.target.value)}
        />
        <input
          type="numeric"
          value={inventario}
          placeholder="Inventario"
          onChange={(e) => setInventario(e.target.value)}
        />

        <button type="submit">Create</button>

        <div className="message">{message ? <p>{message}</p> : null}</div>
      </form>
    </div>
  );
}

export default App;