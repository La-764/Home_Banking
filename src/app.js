const fetchData = async () => {
    try {
      const res = await fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
      const data = await res.json()
      pintarCards(data)
  
    } catch (error) {
      console.log(error)
    }
  }