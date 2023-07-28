import React, { useState } from 'react';
import axios from 'axios';
import styles from './mystyle.module.css'; 

const MyComponent = () => {
  // State variables to store form input values
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [entity, setEntity] = useState('');
  
  // State variable to hold the response data
  const [responseData, setResponseData] = useState({});

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send a POST request to the server with the form data
      const response = await axios.post('/posts', {
        title: title,
        content: content,
        entity: entity,
      });

      // Update the state variable with the response data
      setResponseData(response.data.data);
      console.log(responseData)
      setTitle('');
      setContent('');
      setEntity('');
    } catch (error) {
      // Handle errors if the request fails (e.g., show an error message)
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Search the given song from here</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Term:</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>
        <div>
          <label>Media:</label>
          <textarea value={content} onChange={(e) => setContent(e.target.value)} />
        </div>
        <div className={styles.idiv2}>
          <label>Entity:</label>
          <textarea value={entity} onChange={(e) => setEntity(e.target.value)} />
        </div>
        <button type="submit">Submit</button>
      </form>
      <div>
  {responseData.results && (
    <div>
      <h3>Response Data:</h3>
      <ul className={styles.list}>
        {responseData.results.map((item, index) => (
          <li key={index}>{item.collectionName}</li>
        ))}
      </ul>
    </div>
  )}
</div>
    </div>
  );
};

export default MyComponent;
