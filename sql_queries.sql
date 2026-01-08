-- ============================================================================
-- CUSTOMER CHURN ANALYSIS - SQL QUERIES
-- ============================================================================
-- These queries can be used with any SQL database containing customer data
-- Demonstrates proficiency in SQL for data analysis
-- ============================================================================

-- ============================================================================
-- 1. BASIC DATA EXPLORATION
-- ============================================================================

-- Get total customer count
SELECT COUNT(*) AS total_customers FROM customers;

-- Get churn distribution
SELECT 
    churn,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM customers
GROUP BY churn;

-- ============================================================================
-- 2. CHURN RATE BY DEMOGRAPHICS
-- ============================================================================

-- Churn rate by gender
SELECT 
    gender,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY gender
ORDER BY churn_rate DESC;

-- Churn rate by senior citizen status
SELECT 
    CASE WHEN senior_citizen = 1 THEN 'Senior' ELSE 'Non-Senior' END AS customer_type,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY senior_citizen
ORDER BY churn_rate DESC;

-- ============================================================================
-- 3. CHURN RATE BY SERVICE FEATURES
-- ============================================================================

-- Churn rate by contract type
SELECT 
    contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges
FROM customers
GROUP BY contract
ORDER BY churn_rate DESC;

-- Churn rate by internet service
SELECT 
    internet_service,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY internet_service
ORDER BY churn_rate DESC;

-- Churn rate by payment method
SELECT 
    payment_method,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY payment_method
ORDER BY churn_rate DESC;

-- ============================================================================
-- 4. TENURE ANALYSIS
-- ============================================================================

-- Churn rate by tenure buckets
SELECT 
    CASE 
        WHEN tenure_months <= 12 THEN '0-12 months'
        WHEN tenure_months <= 24 THEN '12-24 months'
        WHEN tenure_months <= 48 THEN '24-48 months'
        ELSE '48+ months'
    END AS tenure_bucket,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY 
    CASE 
        WHEN tenure_months <= 12 THEN '0-12 months'
        WHEN tenure_months <= 24 THEN '12-24 months'
        WHEN tenure_months <= 48 THEN '24-48 months'
        ELSE '48+ months'
    END
ORDER BY 
    CASE tenure_bucket
        WHEN '0-12 months' THEN 1
        WHEN '12-24 months' THEN 2
        WHEN '24-48 months' THEN 3
        ELSE 4
    END;

-- ============================================================================
-- 5. REVENUE ANALYSIS
-- ============================================================================

-- Revenue comparison: churned vs retained
SELECT 
    churn,
    COUNT(*) AS customer_count,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges,
    ROUND(AVG(total_charges), 2) AS avg_total_charges,
    ROUND(SUM(monthly_charges), 2) AS total_monthly_revenue,
    ROUND(SUM(total_charges), 2) AS total_revenue
FROM customers
GROUP BY churn;

-- Revenue at risk from churned customers
SELECT 
    SUM(monthly_charges) AS monthly_revenue_at_risk,
    SUM(monthly_charges) * 12 AS annual_revenue_at_risk
FROM customers
WHERE churn = 'Yes';

-- Top spending churned customers
SELECT 
    customer_id,
    gender,
    tenure_months,
    contract,
    monthly_charges,
    total_charges
FROM customers
WHERE churn = 'Yes'
ORDER BY monthly_charges DESC
LIMIT 10;

-- ============================================================================
-- 6. MULTI-FACTOR ANALYSIS
-- ============================================================================

-- High-risk customer segments (combining multiple factors)
SELECT 
    contract,
    internet_service,
    payment_method,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY contract, internet_service, payment_method
HAVING COUNT(*) >= 5
ORDER BY churn_rate DESC
LIMIT 10;

-- Service bundle analysis
SELECT 
    online_security,
    online_backup,
    device_protection,
    tech_support,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY online_security, online_backup, device_protection, tech_support
HAVING COUNT(*) >= 3
ORDER BY churn_rate DESC;

-- ============================================================================
-- 7. CUSTOMER COHORT ANALYSIS
-- ============================================================================

-- Monthly cohort retention (simplified)
WITH customer_cohorts AS (
    SELECT 
        customer_id,
        tenure_months,
        churn,
        CASE 
            WHEN tenure_months <= 6 THEN 'Very New (0-6m)'
            WHEN tenure_months <= 12 THEN 'New (6-12m)'
            WHEN tenure_months <= 24 THEN 'Established (1-2y)'
            WHEN tenure_months <= 48 THEN 'Loyal (2-4y)'
            ELSE 'Long-term (4y+)'
        END AS cohort
    FROM customers
)
SELECT 
    cohort,
    COUNT(*) AS total,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customer_cohorts
GROUP BY cohort
ORDER BY churn_rate DESC;

-- ============================================================================
-- 8. CUSTOMER LIFETIME VALUE (CLV) ESTIMATION
-- ============================================================================

-- Estimated CLV by customer segment
SELECT 
    contract,
    internet_service,
    ROUND(AVG(tenure_months), 1) AS avg_tenure_months,
    ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges,
    ROUND(AVG(tenure_months * monthly_charges), 2) AS estimated_clv,
    COUNT(*) AS customer_count
FROM customers
WHERE churn = 'No'
GROUP BY contract, internet_service
ORDER BY estimated_clv DESC;

-- ============================================================================
-- 9. PREDICTIVE INDICATORS
-- ============================================================================

-- Customers likely to churn (based on identified risk factors)
SELECT 
    customer_id,
    gender,
    tenure_months,
    contract,
    internet_service,
    payment_method,
    monthly_charges,
    -- Risk score based on multiple factors
    (CASE WHEN contract = 'Month-to-month' THEN 30 ELSE 0 END +
     CASE WHEN internet_service = 'Fiber optic' THEN 20 ELSE 0 END +
     CASE WHEN payment_method = 'Electronic check' THEN 20 ELSE 0 END +
     CASE WHEN tenure_months <= 12 THEN 20 ELSE 0 END +
     CASE WHEN senior_citizen = 1 THEN 10 ELSE 0 END) AS risk_score
FROM customers
WHERE churn = 'No'
ORDER BY risk_score DESC
LIMIT 20;

-- ============================================================================
-- 10. EXECUTIVE SUMMARY QUERIES
-- ============================================================================

-- Key metrics dashboard
SELECT 
    'Total Customers' AS metric,
    COUNT(*) AS value
FROM customers

UNION ALL

SELECT 
    'Churn Rate (%)',
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2)
FROM customers

UNION ALL

SELECT 
    'Average Monthly Charges ($)',
    ROUND(AVG(monthly_charges), 2)
FROM customers

UNION ALL

SELECT 
    'Monthly Revenue at Risk ($)',
    ROUND(SUM(CASE WHEN churn = 'Yes' THEN monthly_charges ELSE 0 END), 2)
FROM customers

UNION ALL

SELECT 
    'Average Tenure (months)',
    ROUND(AVG(tenure_months), 1)
FROM customers;
