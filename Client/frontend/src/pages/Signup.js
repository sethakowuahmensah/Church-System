import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';

function Signup() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email_address: '',
    phone_number: '',
    whatsapp_number: '',
    gender: '',
    age_group: '',
    branch_name: '',
    resident: '',
    marital_status: '',
    is_baptized: false,
    password: '',
    confirm_password: '',
    role: 'member',
  });

  const [errors, setErrors] = useState({});
  const [serverError, setServerError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
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
    setSuccessMessage('');

    const newErrors = {};
    const requiredFields = [
      'first_name',
      'last_name',
      'email_address',
      'gender',
      'age_group',
      'branch_name',
      'password',
      'confirm_password',
    ];

    requiredFields.forEach((field) => {
      if (!formData[field]) {
        newErrors[field] = 'This field is required.';
      }
    });

    if (formData.password && formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters.';
    }

    if (formData.password !== formData.confirm_password) {
      newErrors.confirm_password = 'Passwords do not match.';
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setErrors({});
    setSubmitting(true);

    try {
      const baseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';
      const response = await fetch(`${baseUrl}/api/auth/signup/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setSuccessMessage('Account created successfully. You can now log in.');
        setTimeout(() => {
          navigate('/login');
        }, 1500);
      } else {
        if (data && typeof data === 'object') {
          const apiErrors = {};
          Object.entries(data).forEach(([key, value]) => {
            if (Array.isArray(value)) {
              apiErrors[key] = value[0];
            } else if (typeof value === 'string') {
              apiErrors[key] = value;
            }
          });
          setErrors(apiErrors);
        } else {
          setServerError('Signup failed. Please check your details and try again.');
        }
      }
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
      <div className="auth-card">
        <h1>Create an account</h1>
        <p className="auth-subtitle">
          Join ROYAL GOSPEL CHURCH INTERNATIONAL online to access activities, tithe returns, and more.
        </p>

        {serverError && <div className="auth-alert auth-alert-error">{serverError}</div>}
        {successMessage && <div className="auth-alert auth-alert-success">{successMessage}</div>}

        <form onSubmit={handleSubmit} noValidate>
          <div className="auth-grid">
            <div className="auth-field">
              <label htmlFor="first_name">First name *</label>
              <input
                id="first_name"
                name="first_name"
                type="text"
                value={formData.first_name}
                onChange={handleChange}
              />
              {renderError('first_name')}
            </div>

            <div className="auth-field">
              <label htmlFor="last_name">Last name *</label>
              <input
                id="last_name"
                name="last_name"
                type="text"
                value={formData.last_name}
                onChange={handleChange}
              />
              {renderError('last_name')}
            </div>

            <div className="auth-field">
              <label htmlFor="email_address">Email address *</label>
              <input
                id="email_address"
                name="email_address"
                type="email"
                value={formData.email_address}
                onChange={handleChange}
              />
              {renderError('email_address')}
            </div>

            <div className="auth-field">
              <label htmlFor="phone_number">Phone number</label>
              <input
                id="phone_number"
                name="phone_number"
                type="tel"
                value={formData.phone_number}
                onChange={handleChange}
              />
              {renderError('phone_number')}
            </div>

            <div className="auth-field">
              <label htmlFor="whatsapp_number">WhatsApp number</label>
              <input
                id="whatsapp_number"
                name="whatsapp_number"
                type="tel"
                value={formData.whatsapp_number}
                onChange={handleChange}
              />
              {renderError('whatsapp_number')}
            </div>

            <div className="auth-field">
              <label htmlFor="gender">Gender *</label>
              <select
                id="gender"
                name="gender"
                value={formData.gender}
                onChange={handleChange}
              >
                <option value="">Select gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
              </select>
              {renderError('gender')}
            </div>

            <div className="auth-field">
              <label htmlFor="age_group">Age group *</label>
              <select
                id="age_group"
                name="age_group"
                value={formData.age_group}
                onChange={handleChange}
              >
                <option value="">Select age group</option>
                <option value="youth">Youth</option>
                <option value="children">Children</option>
                <option value="men">Men</option>
                <option value="women">Women</option>
              </select>
              {renderError('age_group')}
            </div>

            <div className="auth-field">
              <label htmlFor="branch_name">Branch *</label>
              <select
                id="branch_name"
                name="branch_name"
                value={formData.branch_name}
                onChange={handleChange}
              >
                <option value="">Select branch</option>
                <option value="Tanokrom">Tanokrom</option>
                <option value="Kwesimintsim">Kwesimintsim</option>
                <option value="Shama">Shama</option>
                <option value="Assakae">Assakae</option>
              </select>
              {renderError('branch_name')}
            </div>

            <div className="auth-field">
              <label htmlFor="resident">Residence</label>
              <input
                id="resident"
                name="resident"
                type="text"
                value={formData.resident}
                onChange={handleChange}
              />
              {renderError('resident')}
            </div>

            <div className="auth-field">
              <label htmlFor="marital_status">Marital status</label>
              <select
                id="marital_status"
                name="marital_status"
                value={formData.marital_status}
                onChange={handleChange}
              >
                <option value="">Select status</option>
                <option value="single">Single</option>
                <option value="married">Married</option>
                <option value="divorced">Divorced</option>
                <option value="widowed">Widowed</option>
              </select>
              {renderError('marital_status')}
            </div>

            <div className="auth-field auth-field-inline">
              <label htmlFor="is_baptized" className="checkbox-label">
                <input
                  id="is_baptized"
                  name="is_baptized"
                  type="checkbox"
                  checked={formData.is_baptized}
                  onChange={handleChange}
                />
                <span>Baptized</span>
              </label>
              {renderError('is_baptized')}
            </div>

            <div className="auth-field">
              <label htmlFor="password">Password *</label>
              <input
                id="password"
                name="password"
                type="password"
                value={formData.password}
                onChange={handleChange}
              />
              {renderError('password')}
            </div>

            <div className="auth-field">
              <label htmlFor="confirm_password">Confirm password *</label>
              <input
                id="confirm_password"
                name="confirm_password"
                type="password"
                value={formData.confirm_password}
                onChange={handleChange}
              />
              {renderError('confirm_password')}
            </div>
          </div>

          <div className="auth-actions">
            <button type="submit" className="btn btn-primary" disabled={submitting}>
              {submitting ? 'Creating account...' : 'Create account'}
            </button>
            <div className="auth-secondary-action">
              Already have an account?{' '}
              <Link to="/login">Log in</Link>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Signup;
