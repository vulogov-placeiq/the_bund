from textx.metamodel import metamodel_from_file
bund_meta = metamodel_from_file('bund.tx')

model = bund_meta.model_from_file('test.bund')

for i in model.functors:
    print i.name,i.__class__.__name__
    for j in i.statements:
        print j.__class__.__name__
        if j.__class__.__name__ == 'Statement':
            print j.call, j.state
            for k in j.state:
                print k, type(k)
        elif j.__class__.__name__ == 'Fact':
            for k in j.fact_elements:
                print k.varname, k.statement, k.state
