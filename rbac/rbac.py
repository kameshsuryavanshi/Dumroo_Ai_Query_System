# import pandas as pd

# def apply_role_filter(df,admin_role):
    
#     filtered_df = df.copy()
#     if 'grade' in admin_role:
#         filtered_df = filtered_df[filtered_df['grade'] == admin_role['grade']]
#     if 'region' in admin_role:
#         filtered_df = filtered_df[filtered_df['region'] == admin_role['region']]
#     if filtered_df.empty:
#         return None
#     return filtered_df


import pandas as pd

def apply_role_filter(df, admin_role):
    """
    Apply role-based filtering to the DataFrame based on admin's grade and region.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        admin_role (dict): Dictionary with 'grade' and 'region' keys
    
    Returns:
        pd.DataFrame: Filtered DataFrame, or None if admin_role is invalid
    """
    if admin_role is None or not isinstance(admin_role, dict):
        print("RBAC: Invalid admin_role, returning None")
        return None
    
    grade = admin_role.get('grade')
    region = admin_role.get('region')
    
    if grade is None or region is None:
        print("RBAC: Missing grade or region, returning None")
        return None
    
    try:
        filtered_df = df[(df['grade'] == grade) & (df['region'] == region)]
        print(f"RBAC: Filtered {len(filtered_df)} rows for grade={grade}, region={region}")
        return filtered_df
    except Exception as e:
        print(f"RBAC: Error filtering DataFrame: {str(e)}")
        return None