import React from 'react';

function UserCard({name,age,email}){
    return <div style={styles.card}>

        <h1 style={styles.title}>Hello , {name}</h1>
        <p style = {styles.description}>Age : {age}</p>
    </div>
}


const styles = {
    card: {
      border: '1px solid #ccc',
      borderRadius: '8px',
      padding: '16px',
      width: '300px',
      textAlign: 'center',
      boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
      color: 'red',
      backgroundColor:'yellow'
    },
    image: {
      width: '100%',
      borderRadius: '8px 8px 0 0',
    },
    title: {
      fontSize: '1.5rem',
      margin: '16px 0',
    },
    description: {
      fontSize: '1rem',
      color: '#555',
    },
    button: {
      padding: '10px 20px',
      backgroundColor: '#007BFF',
      color: '#fff',
      border: 'none',
      borderRadius: '4px',
      cursor: 'pointer',
    },
  };

export default UserCard;