const template = document.getElementById('template').content
const cards=document.getElementById('cards-dolar')
const fragment= document.createDocumentFragment()
document.addEventListener("DOMContentLoaded", () => fetchData());
const fetchData = async () => {
  try {
    const res = await fetch(
      "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
    );
    const data = await res.json();
    console.log(template)
    pintarCards(data)
  } catch (error) {
    console.log(error);
  }
};
const pintarCards = data => {
  const fecha = new Date()
  let variacion
  //  console.log(data);
  data.forEach(item => {
    console.log(item)
    if(item.casa.variacion==undefined){
      variacion='no disponible'
    }
    else{
      variacion=item.casa.variacion
    }
    template.querySelector('.card-title').textContent = item.casa.nombre
    template.querySelector('.compra').textContent = item.casa.compra
    template.querySelector('.venta').textContent = item.casa.venta
    template.querySelector('.card-subtitle').textContent = "variacion: " + variacion
    template.querySelector('.fecha').textContent = fecha.getDate()+'/'+(fecha.getMonth()+1)+'/'+fecha.getFullYear()+' '+fecha.getHours()+':'+fecha.getMinutes()
    const clone = template.cloneNode(true)
    fragment.appendChild(clone)
  });

  cards.appendChild(fragment)
}


