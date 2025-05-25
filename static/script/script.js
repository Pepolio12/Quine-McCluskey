const Minterminos = [];
const DontCare = [];

document.getElementById("Minterminos").addEventListener("keypress",(event) =>{
  if (event.key === 'Enter'){
    const Cantidad = event.target.value;
    if (Cantidad != ""){
      Minterminos.push(Cantidad);
      const Mensaje = "Minterminos: " + Minterminos + ".";
      document.getElementById("Minter").innerHTML = Mensaje;
    }    
    event.target.value = '';
    event.target.focus();
  }
})

document.getElementById("DontCare").addEventListener("keypress",(event) =>{
  if (event.key === 'Enter'){
    const Cantidad1 = event.target.value;
    if (Cantidad1 != ""){
      DontCare.push(Cantidad1);
      const Mensaje = "Don't Care: " + DontCare + ".";
      document.getElementById("Dont").innerHTML = Mensaje;
    }    
    event.target.value = '';
    event.target.focus();
  }
})


document.getElementById("Comenzar").addEventListener("click",()=>{
    fetch('/enviar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({Minterminos, DontCare})
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      Tablas = data.mensaje;
      
      const Key1 = Object.keys(Tablas); // Obtener las claves de cada una de las Tablas
      
      document.getElementById("EcuacionLogica").innerHTML = "RESULTADO:  " + Tablas.Resultado;

      const Tope = "<table><tr><th>Mintermino</th><th>Binario</th><th>Cantidad de 1s</th></tr>";
      let Plantilla = '';

      Plantilla += Tope;
      const Key2 = Object.keys(Tablas["1"]);
      for (let j = 0; j < Key2.length; j++) {
          Plantilla += "<tr><td>"+ Key2[j] + "</td><td>" + Tablas["1"][Key2[j]][0] + "</td><td>"+ Tablas["1"][Key2[j]][0] +"</td></tr>"
        }
      Plantilla += "</table>";

      for (let i = 1; i < (Key1.length)-1; i++) {
        Plantilla += Tope;
        const Key2 = Object.keys(Tablas[Key1[i]]); // Obtener las claves de cada una de las Tablas
        for (let j = 0; j < Key2.length; j++) {
          Plantilla += "<tr><td>"+ Key2[j] + "</td><td>" + Tablas[Key1[i]][Key2[j]][0] + "</td><td>"+ Tablas[Key1[i]][Key2[j]][0] +"</td></tr>"
        }
        Plantilla += "</table>  <hr>";
      }
      document.getElementById("Tablas").innerHTML = Plantilla;

      console.log('Claves en Tablas:', Key1);
      console.log(Tablas["1"][0])
    })
})

