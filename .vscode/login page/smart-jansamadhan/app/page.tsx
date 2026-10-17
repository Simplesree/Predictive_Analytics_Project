import "./App.css";

function App() {
  return (
    <div className="page">

      {/* Navigation Bar */}
      <nav className="navbar">

        <div className="nav-left">
          <a href="#">ABOUT SIH</a>
          <span className="arrow">▼</span>
        </div>

        <div className="nav-item">
          <a href="#">GUIDELINES</a>
          <span className="arrow">▼</span>
        </div>

        <a href="#">PROBLEM STATEMENTS</a>
        <a href="#">KNOW YOUR SPOC</a>
        <a href="#">PROJECT IMPLEMENTATION</a>
        <a href="#">FAQS</a>
        <a href="#">CONTACT US</a>

      </nav>

      {/* Main Section */}
      <main className="hero">

        {/* Jharkhand Government Logo */}
        <div className="logo-container">
          <img
            src="/jharkhand-logo.png"
            alt="Government of Jharkhand"
            className="jharkhand-logo"
          />

          <div className="govt-text">
            GOVERNMENT OF JHARKHAND
          </div>
        </div>

        {/* Heading */}
        <h1>
          SOCIETAL
          <br />
          INNOVATION
        </h1>

        {/* Login Card */}
        <div className="login-box">

          <input
            type="email"
            placeholder="Email"
          />

          <input
            type="password"
            placeholder="Password"
          />

          <select defaultValue="">
            <option value="" disabled>
              Please Select User Role
            </option>

            <option value="citizen">
              Citizen
            </option>

            <option value="admin">
              Administrator
            </option>

            <option value="spoc">
              SPOC
            </option>

            <option value="department">
              Government Department
            </option>
          </select>

          <button>
            Submit
          </button>

          <p className="register-text">
            Don't Have Account?
            <a href="#"> Register Now</a>
          </p>

        </div>

      </main>

    </div>
  );
}

export default App;