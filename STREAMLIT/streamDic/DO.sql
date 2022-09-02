DO
$$
DECLARE
    _schema text;
    _table text;
BEGIN
    FOR _schema, _table IN
        SELECT table_schema, table_name
        FROM information_schema.tables
        -- No filtro por esquema 'public' porque yo uso muchos más esquemas
        WHERE table_type = 'BASE TABLE'
    LOOP
        -- En este bloque LOOP puedes introducir tu código para hacer lo que quieras
        -- con las tablas
        -- Usando las variables _schema, _table
        RAISE NOTICE ' %, %', _schema, _table;
    END LOOP;

END
$$
;
