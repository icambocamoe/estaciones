import React, { useState } from "react";
import {  useNavigate  } from "react-router-dom";
import {
  Container,
  Button,
  Row,
  Col,
  Form,
  FormControl
} from "react-bootstrap";

const Login = () => {
    
    const [info, setInfo] = useState({
      username : "",
      password : ""
    });
  
    const navigate = useNavigate();
    const onChange = e => {
      const value = e.target.value  
      const name = e.target.name  
      setInfo(prevState => ({
          ...prevState,
          [name] : value
      }))
    };

    const onLoginClick = () => {
      console.log(info)
      if(info.username === "admin")
        navigate('./App');
      else
        navigate('./Home');
    };
  
    return (
      <Container>
        <Row>
          <Col md="4">
            <h1>Login</h1>
            <Form>
              <Form.Group controlId="username">
                <Form.Label>User name</Form.Label>
                <Form.Control
                  type="text"
                  name="username"
                  placeholder="Enter user name"
                  onChange={onChange}
                />
                <FormControl.Feedback type="invalid"></FormControl.Feedback>
              </Form.Group>

              <Form.Group controlId="password">
                <Form.Label>Your password</Form.Label>
                <Form.Control
                  type="password"
                  name="password"
                  placeholder="Enter password"
                  onChange={onChange}
                />
                <Form.Control.Feedback type="invalid"></Form.Control.Feedback>
              </Form.Group>
            </Form>
            <Button color="primary" onClick={onLoginClick}>Login</Button>
          </Col>
        </Row>
      </Container>
    );
}

export default Login;