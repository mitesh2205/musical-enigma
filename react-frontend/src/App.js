import React, {
  useState
} from 'react'
import {
  Button
} from 'react-bootstrap'
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Form from 'react-bootstrap/Form';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState([]);

  console.log(result);
  const submitHandler = async (e) => {
    e.preventDefault();
    try {

      const response = await fetch("http://mitesh1234.pythonanywhere.com/", {
        method: "POST",
        body: JSON.stringify({
          "det": text
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Could not fetch Products.");
      }

      setResult(data);
    } catch (error) {
      console.log(error);
    }
  };

  const output = result.map((item) => {
    return (
      <div className="col-6">
        {item[0]} : <h5 className="model_output">{item[1]}</h5>
      </div>
    )
  });
  return (
    <>
      <div className="container pt-5">
        <center>
          <h1 className="pb-3">Example Named Entity</h1>
        </center>
        <Form className="signup-form" onSubmit={submitHandler}>
          <Form.Group>
            <FloatingLabel controlId="floatingTextarea2">
              <Form.Control
                as="textarea"
                placeholder="Leave a comment here"
                style={{ height: '400px' }}
                onChange={(e) => setText(e.target.value)}
              />
            </FloatingLabel>
            <center>
              <Button className="btn btn-secondary mt-3" value="submit" type="submit">Go</Button>
            </center>
          </Form.Group>
        </Form>
        <center>
          <div class="row">
            {output}
          </div>
        </center>
      </div>
    </>
  );
}


export default App;