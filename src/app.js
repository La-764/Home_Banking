document.addEventListener("DOMContentLoaded", () => fetchData());
const dolar=document.getElementById('dolar')
const fetchData = async () => {
  try {
    const res = await fetch(
      "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
    );
    const data = await res.json();
    // laFuncionQueSeCree(data);
  } catch (error) {
    console.log(error);
  }
};

