CREATE TABLE asset (
    id SERIAL PRIMARY KEY, platform VARCHAR(9) NOT NULL, view_date DATE NOT NULL, vin VARCHAR(14) NOT NULL, project_group_title VARCHAR(41) NOT NULL, project_season_title VARCHAR(35), project_single_stop_title VARCHAR(43), asset_playground VARCHAR(16), performance_country_iso2 VARCHAR(2), views NUMERIC(11, 3), total_time_watched NUMERIC(14, 2)
);