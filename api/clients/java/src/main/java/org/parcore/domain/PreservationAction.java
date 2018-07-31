package org.parcore.domain;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.util.ArrayList;
import java.util.List;
import org.threeten.bp.OffsetDateTime;

/**
 * PreservationAction
 */
@SuppressWarnings("unused")
public class PreservationAction {

    @SerializedName("constraints")
    private List<PreservationActionConstraints> constraints = null;

    @SerializedName("description")
    private String description = null;

    @SerializedName("example")
    private String example = null;

    @SerializedName("id")
    private ParIdentifier id = null;

    @SerializedName("inputs")
    private List<InputItem> inputs = new ArrayList<>();

    @SerializedName("localLastModifiedDate")
    private OffsetDateTime localLastModifiedDate = null;

    @SerializedName("outputs")
    private List<OutputItem> outputs = new ArrayList<>();

    @SerializedName("tool")
    private Tool tool = null;

    @SerializedName("type")
    private PreservationActionType type = null;

    public void addConstraintsItem(PreservationActionConstraints constraintsItem) {
        if (this.constraints == null) {
            this.constraints = new ArrayList<>();
        }
        this.constraints.add(constraintsItem);
    }

    /**
     * Get constraints
     * @return constraints
     **/
    @ApiModelProperty(value = "")
    public List<PreservationActionConstraints> getConstraints() {
        return constraints;
    }

    public void setConstraints(List<PreservationActionConstraints> constraints) {
        this.constraints = constraints;
    }

    /**
     * Get description
     * @return description
     **/
    @ApiModelProperty(required = true, value = "")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * Get example
     * @return example
     **/
    @ApiModelProperty(value = "")
    public String getExample() {
        return example;
    }

    public void setExample(String example) {
        this.example = example;
    }

    /**
     * Get id
     * @return id
     **/
    @ApiModelProperty(required = true, value = "")
    public ParIdentifier getId() {
        return id;
    }

    public void setId(ParIdentifier id) {
        this.id = id;
    }

    public void addInputsItem(InputItem inputsItem) {
        this.inputs.add(inputsItem);
    }

    /**
     * Get inputs
     * @return inputs
     **/
    @ApiModelProperty(required = true, value = "")
    public List<InputItem> getInputs() {
        return inputs;
    }

    public void setInputs(List<InputItem> inputs) {
        this.inputs = inputs;
    }

    /**
     * Get localLastModifiedDate
     * @return localLastModifiedDate
     **/
    @ApiModelProperty(value = "")
    public OffsetDateTime getLocalLastModifiedDate() {
        return localLastModifiedDate;
    }

    public void setLocalLastModifiedDate(OffsetDateTime localLastModifiedDate) {
        this.localLastModifiedDate = localLastModifiedDate;
    }

    public void addOutputsItem(OutputItem outputsItem) {
        this.outputs.add(outputsItem);
    }

    /**
     * Get outputs
     * @return outputs
     **/
    @ApiModelProperty(required = true, value = "")
    public List<OutputItem> getOutputs() {
        return outputs;
    }

    public void setOutputs(List<OutputItem> outputs) {
        this.outputs = outputs;
    }

    /**
     * Get tool
     * @return tool
     **/
    @ApiModelProperty(required = true, value = "")
    public Tool getTool() {
        return tool;
    }

    public void setTool(Tool tool) {
        this.tool = tool;
    }

    /**
     * Get type
     * @return type
     **/
    @ApiModelProperty(required = true, value = "")
    public PreservationActionType getType() {
        return type;
    }

    public void setType(PreservationActionType type) {
        this.type = type;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        PreservationAction preservationAction = (PreservationAction) o;
        return Objects.equals(this.constraints, preservationAction.constraints) &&
                Objects.equals(this.description, preservationAction.description) &&
                Objects.equals(this.example, preservationAction.example) &&
                Objects.equals(this.id, preservationAction.id) &&
                Objects.equals(this.inputs, preservationAction.inputs) &&
                Objects.equals(this.localLastModifiedDate, preservationAction.localLastModifiedDate) &&
                Objects.equals(this.outputs, preservationAction.outputs) &&
                Objects.equals(this.tool, preservationAction.tool) &&
                Objects.equals(this.type, preservationAction.type);
    }

    @Override
    public int hashCode() {
        return Objects.hash(constraints, description, example, id, inputs, localLastModifiedDate, outputs, tool, type);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class PreservationAction {\n");

        sb.append("    constraints: ").append(toIndentedString(constraints)).append("\n");
        sb.append("    description: ").append(toIndentedString(description)).append("\n");
        sb.append("    example: ").append(toIndentedString(example)).append("\n");
        sb.append("    id: ").append(toIndentedString(id)).append("\n");
        sb.append("    inputs: ").append(toIndentedString(inputs)).append("\n");
        sb.append("    localLastModifiedDate: ").append(toIndentedString(localLastModifiedDate)).append("\n");
        sb.append("    outputs: ").append(toIndentedString(outputs)).append("\n");
        sb.append("    tool: ").append(toIndentedString(tool)).append("\n");
        sb.append("    type: ").append(toIndentedString(type)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
