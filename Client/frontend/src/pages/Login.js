import React, { useMemo, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

function Login() {
  const navigate = useNavigate();
  const baseUrl = useMemo(
    () => process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000',
    []
  );

  const [formData, setFormData] = useState({
    email_address: '',
    password: '',
    remember: true,
  });
  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState('');
  const [submitting, setSubmitting] = useState(false);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setServerError('');

    const newErrors = {};
    if (!formData.email_address) newErrors.email_address = 'Email is required.';
    if (!formData.password) newErrors.password = 'Password is required.';

    if (Object.keys(newErrors).length) {
      setErrors(newErrors);
      return;
    }

    setErrors({});
    setSubmitting(true);

    try {
      const response = await fetch(`${baseUrl}/api/auth/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email_address: formData.email_address,
          password: formData.password,
        }),
      });

      const data = await response.json().catch(() => null);

      if (!response.ok) {
        if (data && typeof data === 'object') {
          const apiErrors = {};
          Object.entries(data).forEach(([key, value]) => {
            if (Array.isArray(value)) apiErrors[key] = value[0];
            else if (typeof value === 'string') apiErrors[key] = value;
          });
          setErrors(apiErrors);
        } else {
          setServerError('Login failed. Please check your credentials and try again.');
        }
        return;
      }

      // If your API returns tokens/user, you can store them here.
      // Example (optional):
      // if (data?.access) localStorage.setItem('access', data.access);

      navigate('/');
    } catch (err) {
      setServerError('Network error. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  const renderError = (field) => {
    if (!errors[field]) return null;
    return <div className="field-error">{errors[field]}</div>;
  };

  return (
    <div className="auth-page auth-page--bg">
      <div className="auth-card auth-card--compact">
        <div className="auth-header">
          <div className="auth-badge">Welcome back</div>
          <h1>Log in</h1>
          <p className="auth-subtitle">
            Continue to ROYAL GOSPEL CHURCH INTERNATIONAL portal.
          </p>
        </div>

        {serverError && <div className="auth-alert auth-alert-error">{serverError}</div>}

        <form onSubmit={handleSubmit} noValidate>
          <div className="auth-grid auth-grid--single">
            <div className="auth-field">
              <label htmlFor="email_address">Email address</label>
              <input
                id="email_address"
                name="email_address"
                type="email"
                autoComplete="email"
                value={formData.email_address}
                onChange={handleChange}
              />
              {renderError('email_address')}
            </div>

            <div className="auth-field">
              <label htmlFor="password">Password</label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                value={formData.password}
                onChange={handleChange}
              />
              {renderError('password')}
            </div>

            <div className="auth-field auth-field-inline auth-field-inline--spread">
              <label htmlFor="remember" className="checkbox-label">
                <input
                  id="remember"
                  name="remember"
                  type="checkbox"
                  checked={formData.remember}
                  onChange={handleChange}
                />
                <span>Keep me signed in</span>
              </label>
              <span className="auth-microcopy">Secure sign-in</span>
            </div>
          </div>

          <div className="auth-actions">
            <button type="submit" className="btn btn-primary" disabled={submitting}>
              {submitting ? 'Signing in...' : 'Log in'}
            </button>
            <div className="auth-secondary-action">
              New here? <Link to="/signup">Create an account</Link>
            </div>
          </div>
        </form>

        <div className="auth-footer-note">
          By continuing, you agree to respectful use of this platform.
        </div>
      </div>
    </div>
  );
}

export default Login;
