"""
Customer Churn Analysis - Telecom Industry
==========================================
A comprehensive data analysis project demonstrating:
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Visualization
- Business Insights & Recommendations

Author: [Your Name]
Date: January 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# =============================================================================
# 1. DATA LOADING & INITIAL EXPLORATION
# =============================================================================

def load_data(filepath):
    """Load and return the customer dataset."""
    df = pd.read_csv(filepath)
    print("=" * 60)
    print("CUSTOMER CHURN ANALYSIS - TELECOM INDUSTRY")
    print("=" * 60)
    print(f"\n📊 Dataset loaded successfully!")
    print(f"   Total Records: {len(df):,}")
    print(f"   Total Features: {len(df.columns)}")
    return df

def initial_exploration(df):
    """Perform initial data exploration."""
    print("\n" + "=" * 60)
    print("1. INITIAL DATA EXPLORATION")
    print("=" * 60)
    
    print("\n📋 Dataset Shape:", df.shape)
    print("\n📋 Column Data Types:")
    print(df.dtypes)
    
    print("\n📋 First 5 Records:")
    print(df.head())
    
    print("\n📋 Statistical Summary:")
    print(df.describe())
    
    return df

# =============================================================================
# 2. DATA CLEANING & PREPROCESSING
# =============================================================================

def clean_data(df):
    """Clean and preprocess the dataset."""
    print("\n" + "=" * 60)
    print("2. DATA CLEANING & PREPROCESSING")
    print("=" * 60)
    
    # Check for missing values
    missing = df.isnull().sum()
    print("\n🔍 Missing Values Check:")
    if missing.sum() == 0:
        print("   ✅ No missing values found!")
    else:
        print(missing[missing > 0])
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"\n🔍 Duplicate Records: {duplicates}")
    if duplicates > 0:
        df = df.drop_duplicates()
        print(f"   ✅ Removed {duplicates} duplicate records")
    
    # Convert churn to binary
    df['churn_numeric'] = df['churn'].map({'Yes': 1, 'No': 0})
    
    # Create tenure categories
    df['tenure_category'] = pd.cut(df['tenure_months'], 
                                    bins=[0, 12, 24, 48, 72],
                                    labels=['0-12 months', '12-24 months', 
                                           '24-48 months', '48+ months'])
    
    # Create monthly charges categories
    df['charges_category'] = pd.cut(df['monthly_charges'],
                                     bins=[0, 50, 75, 100, 150],
                                     labels=['Low', 'Medium', 'High', 'Premium'])
    
    print("\n✅ Data cleaning completed!")
    print(f"   Added 'churn_numeric' column")
    print(f"   Added 'tenure_category' column")
    print(f"   Added 'charges_category' column")
    
    return df

# =============================================================================
# 3. EXPLORATORY DATA ANALYSIS (EDA)
# =============================================================================

def churn_analysis(df):
    """Analyze overall churn rate."""
    print("\n" + "=" * 60)
    print("3. CHURN RATE ANALYSIS")
    print("=" * 60)
    
    churn_counts = df['churn'].value_counts()
    churn_pct = df['churn'].value_counts(normalize=True) * 100
    
    print("\n📊 Overall Churn Distribution:")
    print(f"   Retained Customers: {churn_counts['No']:,} ({churn_pct['No']:.1f}%)")
    print(f"   Churned Customers:  {churn_counts['Yes']:,} ({churn_pct['Yes']:.1f}%)")
    
    # Churn rate calculation
    churn_rate = (df['churn'] == 'Yes').mean() * 100
    print(f"\n⚠️  CHURN RATE: {churn_rate:.1f}%")
    
    return churn_rate

def demographic_analysis(df):
    """Analyze churn by demographic factors."""
    print("\n" + "=" * 60)
    print("4. DEMOGRAPHIC ANALYSIS")
    print("=" * 60)
    
    # Gender analysis
    gender_churn = df.groupby('gender')['churn_numeric'].mean() * 100
    print("\n👥 Churn Rate by Gender:")
    for gender, rate in gender_churn.items():
        print(f"   {gender}: {rate:.1f}%")
    
    # Senior citizen analysis
    senior_churn = df.groupby('senior_citizen')['churn_numeric'].mean() * 100
    print("\n👴 Churn Rate by Senior Citizen Status:")
    print(f"   Non-Senior (0): {senior_churn[0]:.1f}%")
    print(f"   Senior (1):     {senior_churn[1]:.1f}%")
    
    # Partner analysis
    partner_churn = df.groupby('partner')['churn_numeric'].mean() * 100
    print("\n💑 Churn Rate by Partner Status:")
    for status, rate in partner_churn.items():
        print(f"   {status}: {rate:.1f}%")
    
    return gender_churn, senior_churn, partner_churn

def service_analysis(df):
    """Analyze churn by service features."""
    print("\n" + "=" * 60)
    print("5. SERVICE ANALYSIS")
    print("=" * 60)
    
    # Internet service analysis
    internet_churn = df.groupby('internet_service')['churn_numeric'].mean() * 100
    print("\n🌐 Churn Rate by Internet Service:")
    for service, rate in internet_churn.items():
        print(f"   {service}: {rate:.1f}%")
    
    # Contract analysis
    contract_churn = df.groupby('contract')['churn_numeric'].mean() * 100
    print("\n📝 Churn Rate by Contract Type:")
    for contract, rate in contract_churn.items():
        print(f"   {contract}: {rate:.1f}%")
    
    # Payment method analysis
    payment_churn = df.groupby('payment_method')['churn_numeric'].mean() * 100
    print("\n💳 Churn Rate by Payment Method:")
    for method, rate in payment_churn.items():
        print(f"   {method}: {rate:.1f}%")
    
    return internet_churn, contract_churn, payment_churn

def tenure_revenue_analysis(df):
    """Analyze tenure and revenue patterns."""
    print("\n" + "=" * 60)
    print("6. TENURE & REVENUE ANALYSIS")
    print("=" * 60)
    
    # Tenure category analysis
    tenure_churn = df.groupby('tenure_category')['churn_numeric'].mean() * 100
    print("\n📅 Churn Rate by Tenure:")
    for tenure, rate in tenure_churn.items():
        print(f"   {tenure}: {rate:.1f}%")
    
    # Average monthly charges
    avg_charges_churned = df[df['churn'] == 'Yes']['monthly_charges'].mean()
    avg_charges_retained = df[df['churn'] == 'No']['monthly_charges'].mean()
    
    print(f"\n💰 Average Monthly Charges:")
    print(f"   Churned Customers:  ${avg_charges_churned:.2f}")
    print(f"   Retained Customers: ${avg_charges_retained:.2f}")
    
    # Revenue at risk
    revenue_at_risk = df[df['churn'] == 'Yes']['monthly_charges'].sum()
    total_revenue = df['monthly_charges'].sum()
    
    print(f"\n⚠️  Monthly Revenue at Risk: ${revenue_at_risk:,.2f}")
    print(f"   ({(revenue_at_risk/total_revenue)*100:.1f}% of total monthly revenue)")
    
    return tenure_churn

# =============================================================================
# 4. STATISTICAL ANALYSIS
# =============================================================================

def statistical_tests(df):
    """Perform statistical tests."""
    print("\n" + "=" * 60)
    print("7. STATISTICAL ANALYSIS")
    print("=" * 60)
    
    # T-test for monthly charges between churned and retained
    churned_charges = df[df['churn'] == 'Yes']['monthly_charges']
    retained_charges = df[df['churn'] == 'No']['monthly_charges']
    
    t_stat, p_value = stats.ttest_ind(churned_charges, retained_charges)
    
    print("\n📈 T-Test: Monthly Charges (Churned vs Retained)")
    print(f"   T-statistic: {t_stat:.4f}")
    print(f"   P-value: {p_value:.4f}")
    if p_value < 0.05:
        print("   ✅ Statistically significant difference (p < 0.05)")
    else:
        print("   ❌ No statistically significant difference")
    
    # Chi-square test for contract type and churn
    contingency = pd.crosstab(df['contract'], df['churn'])
    chi2, p_chi, dof, expected = stats.chi2_contingency(contingency)
    
    print("\n📈 Chi-Square Test: Contract Type vs Churn")
    print(f"   Chi-square statistic: {chi2:.4f}")
    print(f"   P-value: {p_chi:.4f}")
    print(f"   Degrees of freedom: {dof}")
    if p_chi < 0.05:
        print("   ✅ Significant relationship exists (p < 0.05)")
    else:
        print("   ❌ No significant relationship")
    
    # Correlation analysis
    print("\n📈 Correlation Analysis:")
    correlation = df['tenure_months'].corr(df['churn_numeric'])
    print(f"   Tenure vs Churn: {correlation:.4f}")
    
    correlation2 = df['monthly_charges'].corr(df['churn_numeric'])
    print(f"   Monthly Charges vs Churn: {correlation2:.4f}")

# =============================================================================
# 5. DATA VISUALIZATION
# =============================================================================

def create_visualizations(df, save_path='visualizations/'):
    """Create and save all visualizations."""
    import os
    os.makedirs(save_path, exist_ok=True)
    
    print("\n" + "=" * 60)
    print("8. CREATING VISUALIZATIONS")
    print("=" * 60)
    
    # Figure 1: Churn Distribution
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Pie chart
    colors = ['#2ecc71', '#e74c3c']
    df['churn'].value_counts().plot(kind='pie', ax=axes[0], autopct='%1.1f%%',
                                     colors=colors, startangle=90)
    axes[0].set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('')
    
    # Bar chart
    sns.countplot(data=df, x='churn', palette=colors, ax=axes[1])
    axes[1].set_title('Churn Count', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Churn Status')
    axes[1].set_ylabel('Number of Customers')
    
    # Add count labels
    for p in axes[1].patches:
        axes[1].annotate(f'{int(p.get_height())}', 
                         (p.get_x() + p.get_width()/2., p.get_height()),
                         ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{save_path}01_churn_distribution.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 01_churn_distribution.png")
    
    # Figure 2: Churn by Contract Type
    fig, ax = plt.subplots(figsize=(10, 6))
    contract_churn = df.groupby(['contract', 'churn']).size().unstack()
    contract_churn.plot(kind='bar', ax=ax, color=['#2ecc71', '#e74c3c'])
    ax.set_title('Churn by Contract Type', fontsize=14, fontweight='bold')
    ax.set_xlabel('Contract Type')
    ax.set_ylabel('Number of Customers')
    ax.legend(['Retained', 'Churned'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{save_path}02_churn_by_contract.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 02_churn_by_contract.png")
    
    # Figure 3: Monthly Charges Distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x='monthly_charges', hue='churn', 
                 palette=['#2ecc71', '#e74c3c'], kde=True, ax=ax)
    ax.set_title('Monthly Charges Distribution by Churn Status', 
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Monthly Charges ($)')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f'{save_path}03_charges_distribution.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 03_charges_distribution.png")
    
    # Figure 4: Tenure vs Churn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='churn', y='tenure_months', 
                palette=['#2ecc71', '#e74c3c'], ax=ax)
    ax.set_title('Customer Tenure by Churn Status', fontsize=14, fontweight='bold')
    ax.set_xlabel('Churn Status')
    ax.set_ylabel('Tenure (Months)')
    plt.tight_layout()
    plt.savefig(f'{save_path}04_tenure_boxplot.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 04_tenure_boxplot.png")
    
    # Figure 5: Heatmap - Service Features vs Churn
    fig, ax = plt.subplots(figsize=(12, 8))
    
    services = ['online_security', 'online_backup', 'device_protection', 
                'tech_support', 'streaming_tv', 'streaming_movies']
    
    churn_by_service = df.groupby('churn')[services].apply(
        lambda x: (x == 'Yes').sum() / len(x) * 100
    ).T
    
    sns.heatmap(churn_by_service, annot=True, fmt='.1f', cmap='RdYlGn_r',
                ax=ax, cbar_kws={'label': 'Percentage (%)'})
    ax.set_title('Service Adoption Rate by Churn Status', fontsize=14, fontweight='bold')
    ax.set_ylabel('Service')
    plt.tight_layout()
    plt.savefig(f'{save_path}05_service_heatmap.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 05_service_heatmap.png")
    
    # Figure 6: Payment Method Analysis
    fig, ax = plt.subplots(figsize=(12, 6))
    payment_churn = df.groupby('payment_method')['churn_numeric'].mean() * 100
    payment_churn.sort_values(ascending=True).plot(kind='barh', ax=ax, 
                                                    color='#3498db')
    ax.set_title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
    ax.set_xlabel('Churn Rate (%)')
    ax.set_ylabel('Payment Method')
    
    # Add percentage labels
    for i, v in enumerate(payment_churn.sort_values(ascending=True)):
        ax.text(v + 0.5, i, f'{v:.1f}%', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{save_path}06_payment_method_churn.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 06_payment_method_churn.png")
    
    # Figure 7: Comprehensive Dashboard
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('CUSTOMER CHURN ANALYSIS DASHBOARD', fontsize=16, fontweight='bold')
    
    # 1. Churn Rate Pie
    df['churn'].value_counts().plot(kind='pie', ax=axes[0, 0], autopct='%1.1f%%',
                                     colors=['#2ecc71', '#e74c3c'], startangle=90)
    axes[0, 0].set_title('Overall Churn Rate')
    axes[0, 0].set_ylabel('')
    
    # 2. Churn by Internet Service
    internet_churn = df.groupby('internet_service')['churn_numeric'].mean() * 100
    internet_churn.plot(kind='bar', ax=axes[0, 1], color='#9b59b6')
    axes[0, 1].set_title('Churn by Internet Service')
    axes[0, 1].set_ylabel('Churn Rate (%)')
    axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45)
    
    # 3. Tenure Distribution
    sns.histplot(data=df, x='tenure_months', hue='churn', ax=axes[0, 2],
                 palette=['#2ecc71', '#e74c3c'], kde=True)
    axes[0, 2].set_title('Tenure Distribution')
    
    # 4. Contract Type
    contract_churn = df.groupby('contract')['churn_numeric'].mean() * 100
    contract_churn.plot(kind='bar', ax=axes[1, 0], color=['#e74c3c', '#f39c12', '#2ecc71'])
    axes[1, 0].set_title('Churn by Contract')
    axes[1, 0].set_ylabel('Churn Rate (%)')
    axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45)
    
    # 5. Monthly Charges Box Plot
    sns.boxplot(data=df, x='churn', y='monthly_charges', ax=axes[1, 1],
                palette=['#2ecc71', '#e74c3c'])
    axes[1, 1].set_title('Monthly Charges Distribution')
    
    # 6. Senior Citizen Analysis
    senior_data = df.groupby(['senior_citizen', 'churn']).size().unstack()
    senior_data.plot(kind='bar', ax=axes[1, 2], color=['#2ecc71', '#e74c3c'])
    axes[1, 2].set_title('Churn by Senior Status')
    axes[1, 2].set_xticklabels(['Non-Senior', 'Senior'], rotation=0)
    
    plt.tight_layout()
    plt.savefig(f'{save_path}07_dashboard.png', dpi=300, bbox_inches='tight')
    print("   ✅ Saved: 07_dashboard.png")
    
    print("\n✅ All visualizations saved to 'visualizations/' folder")
    
    plt.close('all')

# =============================================================================
# 6. KEY INSIGHTS & RECOMMENDATIONS
# =============================================================================

def generate_insights(df):
    """Generate key insights and recommendations."""
    print("\n" + "=" * 60)
    print("9. KEY INSIGHTS & BUSINESS RECOMMENDATIONS")
    print("=" * 60)
    
    churn_rate = (df['churn'] == 'Yes').mean() * 100
    
    # Calculate key metrics
    mtm_churn = df[df['contract'] == 'Month-to-month']['churn_numeric'].mean() * 100
    fiber_churn = df[df['internet_service'] == 'Fiber optic']['churn_numeric'].mean() * 100
    senior_churn = df[df['senior_citizen'] == 1]['churn_numeric'].mean() * 100
    electronic_churn = df[df['payment_method'] == 'Electronic check']['churn_numeric'].mean() * 100
    new_customer_churn = df[df['tenure_months'] <= 12]['churn_numeric'].mean() * 100
    
    print("\n🔍 KEY FINDINGS:")
    print("-" * 50)
    print(f"""
    1. OVERALL CHURN RATE: {churn_rate:.1f}%
       - This represents significant revenue leakage
       
    2. HIGH-RISK SEGMENTS IDENTIFIED:
       
       📌 Contract Type:
       - Month-to-month customers: {mtm_churn:.1f}% churn rate
       - Long-term contracts show much lower churn
       
       📌 Internet Service:
       - Fiber optic customers: {fiber_churn:.1f}% churn rate
       - May indicate service quality issues
       
       📌 Demographics:
       - Senior citizens: {senior_churn:.1f}% churn rate
       - May need dedicated support programs
       
       📌 Payment Method:
       - Electronic check users: {electronic_churn:.1f}% churn rate
       - Autopay could improve retention
       
       📌 Tenure:
       - New customers (0-12 months): {new_customer_churn:.1f}% churn rate
       - Critical onboarding period
    """)
    
    print("\n💡 STRATEGIC RECOMMENDATIONS:")
    print("-" * 50)
    print("""
    1. INCENTIVIZE LONG-TERM CONTRACTS
       - Offer discounts for 1-year and 2-year commitments
       - Create loyalty programs with milestone rewards
       
    2. IMPROVE FIBER OPTIC SERVICE
       - Investigate service quality issues
       - Implement proactive support for fiber customers
       - Consider satisfaction surveys
       
    3. SENIOR CITIZEN PROGRAM
       - Create dedicated support channels
       - Simplify billing and service options
       - Offer personalized assistance
       
    4. PAYMENT METHOD OPTIMIZATION
       - Incentivize auto-pay enrollment
       - Offer small discounts for credit card/bank transfer
       
    5. NEW CUSTOMER RETENTION
       - Implement 90-day onboarding program
       - Proactive check-ins during first year
       - Early warning system for at-risk customers
       
    6. PREDICTIVE CHURN MODEL
       - Build ML model to identify at-risk customers
       - Enable proactive intervention
       - Personalized retention offers
    """)
    
    # Revenue Impact
    avg_monthly_churned = df[df['churn'] == 'Yes']['monthly_charges'].mean()
    churned_count = (df['churn'] == 'Yes').sum()
    monthly_revenue_loss = avg_monthly_churned * churned_count
    annual_revenue_loss = monthly_revenue_loss * 12
    
    print("\n💰 REVENUE IMPACT ANALYSIS:")
    print("-" * 50)
    print(f"""
    • Churned Customers: {churned_count}
    • Avg Monthly Revenue per Churned Customer: ${avg_monthly_churned:.2f}
    • Estimated Monthly Revenue Loss: ${monthly_revenue_loss:,.2f}
    • Projected Annual Revenue Loss: ${annual_revenue_loss:,.2f}
    
    ⚠️  Reducing churn by just 5% could save ~${annual_revenue_loss * 0.05:,.2f}/year
    """)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main execution function."""
    # Load data
    df = load_data('data/telecom_customers.csv')
    
    # Initial exploration
    df = initial_exploration(df)
    
    # Clean data
    df = clean_data(df)
    
    # Perform analysis
    churn_analysis(df)
    demographic_analysis(df)
    service_analysis(df)
    tenure_revenue_analysis(df)
    
    # Statistical analysis
    statistical_tests(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Generate insights
    generate_insights(df)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\n📁 Files generated:")
    print("   • visualizations/01_churn_distribution.png")
    print("   • visualizations/02_churn_by_contract.png")
    print("   • visualizations/03_charges_distribution.png")
    print("   • visualizations/04_tenure_boxplot.png")
    print("   • visualizations/05_service_heatmap.png")
    print("   • visualizations/06_payment_method_churn.png")
    print("   • visualizations/07_dashboard.png")
    
    return df

if __name__ == "__main__":
    df = main()
